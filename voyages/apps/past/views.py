from django.core.paginator import Paginator
from django.http import JsonResponse
from voyages.apps.past.models import *
import json

def search_enslaved(request):
    # A little bit of Python magic where we pass the dictionary
    # decoded from the JSON body as arguments to the EnslavedSearch
    # constructor.
    data = json.loads(request.body)
    search = EnslavedSearch(**data.search_query)
    _fields = ['enslaved_id', 'modern_name_first', 'modern_name_second', 'modern_name_third',
        'age', 'gender', 'height', 'ethnicity__name', 'language_group__name', 'country__name',
        'voyage__id']
    query = search.execute().values(_fields)
    output_type = data.get('output', 'resultsTable')
    # For now we only support outputing the results to DataTables.
    if output_type == 'resultsTable':
        table_params = {}
        try:
            table_params = data['tableParams']
            rows_per_page = int(table_params['length'])
            current_page_num = 1 + int(table_params['start']) / rows_per_page
            paginator = Paginator(query, rows_per_page)
            page = paginator.page(current_page_num)
        except:
            page = query
        pass
        reponse_data = {}
        total_results = query.count()
        reponse_data['recordsTotal'] = total_results
        reponse_data['recordsFiltered'] = total_results
        reponse_data['draw'] = int(table_params.get('draw', 0))
        reponse_data['data'] = list(page)
        return JsonResponse(reponse_data)
    return JsonResponse({'error': 'Unsupported'})