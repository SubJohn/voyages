from django.db import transaction
from voyages.apps.contribute.models import *
from voyages.apps.contribute.views import full_contribution_id, get_contribution_from_id, get_filtered_contributions
from voyages.apps.voyage.models import *
import csv

def export_accepted_contributions_to_csv(csvfile):
    data = export_accepted_contributions()
    fields = ['ADLT1IMP', 'ADLT2IMP', 'ADLT3IMP', 'ADPSALE1', 'ADPSALE2', 
        'ADULT1', 'ADULT2', 'ADULT3', 'ADULT4', 'ADULT5', 'ADULT6', 'ADULT7',
        'ARRPORT', 'ARRPORT2', 'BOY1', 'BOY2', 'BOY3', 'BOY4', 'BOY5', 'BOY6',
        'BOY7', 'BOYRAT1', 'BOYRAT3', 'BOYRAT7', 'CAPTAINA', 'CAPTAINB',
        'CAPTAINC', 'CHIL1IMP', 'CHIL2IMP', 'CHIL3IMP', 'CHILD1', 'CHILD2',
        'CHILD3', 'CHILD4', 'CHILD5', 'CHILD6', 'CHILD7', 'CHILRAT1',
        'CHILRAT3', 'CHILRAT7', 'CONSTREG', 'CREW', 'CREW1', 'CREW2', 'CREW3',
        'CREW4', 'CREW5', 'CREWDIED', 'DATEDEPA', 'DATEDEPB', 'DATEDEPC',
        'D1SLATRA', 'D1SLATRB', 'D1SLATRC', 'DLSLATRA', 'DLSLATRB',
        'DLSLATRC', 'DDEPAM', 'DDEPAMB', 'DDEPAMC', 'DATARR32', 'DATARR33',
        'DATARR34', 'DATARR36', 'DATARR37', 'DATARR38', 'DATARR39', 'DATARR40',
        'DATARR41', 'DATARR43', 'DATARR44', 'DATARR45', 'DATEDEP', 'DATEBUY',
        'DATELEFTAFR', 'DATELAND1', 'DATELAND2', 'DATELAND3', 'DATEDEPAM',
        'DATEEND', 'DEPTREGIMP', 'DEPTREGIMP1', 'EMBPORT', 'EMBPORT2',
        'EMBREG', 'EMBREG2', 'EVGREEN', 'FATE', 'FATE2', 'FATE3', 'FATE4',
        'FEMALE1', 'FEMALE2', 'FEMALE3', 'FEMALE4', 'FEMALE5', 'FEMALE6',
        'FEMALE7', 'FEML1IMP', 'FEML2IMP', 'FEML3IMP', 'GIRL1', 'GIRL2',
        'GIRL3', 'GIRL4', 'GIRL5', 'GIRL6', 'GIRL7', 'GIRLRAT1', 'GIRLRAT3',
        'GIRLRAT7', 'GUNS', 'INFANT1', 'INFANT3', 'INFANT4', 'JAMCASPR',
        'MAJBUYPT', 'MAJBYIMP', 'MAJBYIMP1', 'MAJSELPT', 'MALE1', 'MALE1IMP',
        'MALE2', 'MALE2IMP', 'MALE3', 'MALE3IMP', 'MALE4', 'MALE5', 'MALE6',
        'MALE7', 'MALRAT1', 'MALRAT3', 'MALRAT7', 'MEN1', 'MEN2', 'MEN3',
        'MEN4', 'MEN5', 'MEN6', 'MEN7', 'MENRAT1', 'MENRAT3', 'MENRAT7',
        'MJBYPTIMP', 'MJSELIMP', 'MJSELIMP1', 'MJSLPTIMP', 'NATINIMP',
        'NATIONAL', 'NCAR13', 'NCAR15', 'NCAR17', 'NDESERT', 'NPAFTTRA',
        'NPPRETRA', 'NPPRIOR', 'OWNERA', 'OWNERB', 'OWNERC', 'OWNERD',
        'OWNERE', 'OWNERF', 'OWNERG', 'OWNERH', 'OWNERI', 'OWNERJ', 'OWNERK',
        'OWNERL', 'OWNERM', 'OWNERN', 'OWNERO', 'OWNERP', 'PLAC1TRA',
        'PLAC2TRA', 'PLAC3TRA', 'PLACCONS', 'PLACREG', 'PORTDEP', 'PORTRET',
        'PTDEPIMP', 'REGARR', 'REGARR2', 'REGDIS1', 'REGDIS2', 'REGDIS3',
        'REGEM1', 'REGEM2', 'REGEM3', 'REGISREG', 'RESISTANCE', 'RETRNREG',
        'RETRNREG1', 'RIG', 'SAILD1', 'SAILD2', 'SAILD3', 'SAILD4', 'SAILD5',
        'SHIPNAME', 'SLA1PORT', 'SLAARRIV', 'SLADAFRI', 'SLADAMER', 'SLADVOY',
        'SLAMIMP', 'SLAS32', 'SLAS36', 'SLAS39', 'SLAVEMA1', 'SLAVEMA3',
        'SLAVEMA7', 'SLAVEMX1', 'SLAVEMX3', 'SLAVEMX7', 'SLAVMAX1', 'SLAVMAX3',
        'SLAVMAX7', 'SLAXIMP', 'SLINTEN2', 'SLINTEND', 'SOURCEA', 'SOURCEB',
        'SOURCEC', 'SOURCED', 'SOURCEE', 'SOURCEF', 'SOURCEG', 'SOURCEH',
        'SOURCEI', 'SOURCEJ', 'SOURCEK', 'SOURCEL', 'SOURCEM', 'SOURCEN',
        'SOURCEO', 'SOURCEP', 'SOURCEQ', 'SOURCER', 'TONMOD', 'TONNAGE',
        'TONTYPE', 'TSLAVESD', 'TSLAVESP', 'TSLMTIMP', 'VOY1IMP', 'VOY2IMP',
        'VOYAGE', 'VYMRTIMP', 'VYMRTRAT', 'WOMEN1', 'WOMEN2', 'WOMEN3',
        'WOMEN4', 'WOMEN5', 'WOMEN6', 'WOMEN7', 'WOMRAT1', 'WOMRAT3', 'WOMRAT7',
        'XMIMPFLAG', 'YEAR10', 'YEAR100', 'YEAR25', 'YEAR5', 'YEARAF', 'YEARAM',
        'YEARDEP', 'YRCONS', 'YRREG']
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    for item in data:
        writer.writerow(item)

def export_accepted_contributions():
    """
    Produce a list of dicts, each representing an accepted contribution.
    """
    review_requests = _fetch_accepted_reviews()
    result = []
    for req in review_requests:    
        editor_contribution = req.editor_contribution.first()
        if editor_contribution is None or editor_contribution.interim_voyage is None: continue
        result.append(_map_interim_to_spss(editor_contribution.interim_voyage))
    return result

def publish_accepted_contributions(log_file):
    """
    Publish all accepted contributions and use the
    given log_file to register the progress. Since
    all the db operations are transacional, either
    everything is published or nothing is.
    """
    import os
    
    def log(text):     
        log_file.write(text)
        log_file.flush()
        os.fsync(log_file.fileno())
        
    log('Backing up all data.\n')

    # Step 1 - Backup database
    os.system('python manage.py dumpdata > /var/tmp/db.json')

    log('Finished backup.\n')
    log('Fetching contributions...\n')
    review_requests = _fetch_accepted_reviews()
    log('Publishing...\n')
    # Step 2 - Publish database
    try:
        with transaction.atomic():
            count = 0
            for req in review_requests:
                # Basic validation.
                count += 1
                log('Processing ' + req.contribution_id + '\n')
                if req.final_decision != ReviewRequestDecision.accepted_by_editor:
                    raise Exception('Review cannot be published since it was not accepted by editor')
                if req.contribution_id.startswith('delete'):
                    _publish_single_review_delete(req)
                elif req.contribution_id.startswith('merge'):
                    _publish_single_review_merge(req)
                elif req.contribution_id.startswith('new'):
                    _publish_single_review_new(req)
                elif req.contribution_id.startswith('edit'):
                    _publish_single_review_update(req)
                else:
                    raise Exception('Unexpected contribution type')
                req.archived = True
                req.save()
        log('Finished all publications.\n')
        log('Total published: ' + str(count) + '.\n')
        # Step 3 - update solr index.
        log('Updating solr index.\n')
        os.system('python manage.py update_index voyage.voyage --age 24')
        log('Solr index is now updated.\n')
        return True
    except Exception as exception:
        log('An error occurred. Database transaction was rolledback.\n')
        log(str(exception))
        import traceback
        log(traceback.format_exc())
        return False
    finally:
        log('EOF')
        log_file.close()

def _delete_child_fk(obj, child_attr):
    child = getattr(obj, child_attr)
    if child:
        setattr(obj, child_attr, None)
        obj.save()
        child.delete()
        
def _fetch_accepted_reviews():
    contribution_info = get_filtered_contributions({'status': ContributionStatus.approved})
    review_requests = []
    for info in contribution_info:
        reqs = list(ReviewRequest.objects.filter(contribution_id=full_contribution_id(info['type'], info['id']), archived=False))
        if len(reqs) != 1:
            raise Exception('Expected a single active review request for approved contributions')
        review_requests.append(reqs[0])
    return review_requests

def _map_interim_to_spss(interim):
    data = {}
    
    def map_csv_date(varname, csv_date, labels=['A', 'B', 'C']):
        members = csv_date.split(',')
        if len(members) != 3:
            members = [None, None, None]
        data[varname + labels[0]] = int(members[1]) if members[1] != '' else None
        data[varname + labels[1]] = int(members[0]) if members[0] != '' else None
        data[varname + labels[2]] = int(members[2]) if members[2] != '' else None
    
    map_csv_date('DATEDEP', interim.date_departure)
    map_csv_date('D1SLATR', interim.date_slave_purchase_began)
    map_csv_date('DLSLATR', interim.date_vessel_left_last_slaving_port)
    map_csv_date('DATARR3', interim.date_first_slave_disembarkation, '234')
    map_csv_date('DATARR3', interim.date_second_slave_disembarkation, '678')
    map_csv_date('DATARR', interim.date_third_slave_disembarkation, ['39', '40', '41'])
    map_csv_date('DDEPAM', interim.date_return_departure, ['', 'B', 'C'])
    map_csv_date('DATARR4', interim.date_voyage_completed, '345')
    data['VOYAGE'] = interim.length_of_middle_passage
    
    def get_value(x):
        return x.value if x else None
    
    def get_region(place):
        return place.region.value if place else None
    
    # Ship, nation, owners
    data['SHIPNAME'] = interim.name_of_vessel
    data['NATIONAL'] = get_value(interim.national_carrier)
    data['TONNAGE'] = interim.tonnage_of_vessel
    data['TONTYPE'] = get_value(interim.ton_type)
    data['RIG'] = get_value(interim.rig_of_vessel)
    data['GUNS'] = interim.guns_mounted
    data['YRCONS'] = interim.year_ship_constructed
    data['PLACCONS'] = get_value(interim.ship_construction_place)
    data['CONSTREG'] = get_region(interim.ship_construction_place)
    data['YRREG'] = interim.year_ship_registered
    data['PLACREG'] = get_value(interim.ship_registration_place)
    data['REGISREG'] = get_region(interim.ship_registration_place)
    data['OWNERA'] = interim.first_ship_owner
    data['OWNERB'] = interim.second_ship_owner
    other_ship_owners = interim.additional_ship_owners.split('\n')
    aux = 'CDEFGHIJKLMNOP'
    for i, owner in enumerate(other_ship_owners):
        if i >= len(aux): break
        data['OWNER' + aux[i]] = owner
       
    data['CAPTAINA'] = interim.first_captain    
    data['CAPTAINB'] = interim.second_captain    
    data['CAPTAINC'] = interim.third_captain
    
    # Outcome
    data['FATE'] = get_value(interim.voyage_outcome)
    data['RESISTANCE'] = get_value(interim.african_resistance)
    
    # Itinerary    
    data['PORTDEP'] = get_value(interim.port_of_departure)
    data['EMBPORT'] = get_value(interim.first_port_intended_embarkation)
    data['EMBPORT2'] = get_value(interim.second_port_intended_embarkation)
    data['EMBREG'] = get_region(interim.first_port_intended_embarkation)
    data['EMBREG2'] = get_region(interim.second_port_intended_embarkation)
    data['ARRPORT'] = get_value(interim.first_port_intended_disembarkation)
    data['ARRPORT2'] = get_value(interim.second_port_intended_disembarkation)
    data['REGARR'] = get_region(interim.first_port_intended_disembarkation)
    data['REGARR2'] = get_region(interim.second_port_intended_disembarkation)
    data['NPPRETRA'] = interim.number_of_ports_called_prior_to_slave_purchase
    data['PLAC1TRA'] = get_value(interim.first_place_of_slave_purchase)
    data['PLAC2TRA'] = get_value(interim.second_place_of_slave_purchase)
    data['PLAC3TRA'] = get_value(interim.third_place_of_slave_purchase)
    data['REGEM1'] = get_region(interim.first_place_of_slave_purchase)
    data['REGEM2'] = get_region(interim.second_place_of_slave_purchase)
    data['REGEM3'] = get_region(interim.third_place_of_slave_purchase)
    data['NPAFTTRA'] = get_value(interim.place_of_call_before_atlantic_crossing)
    data['NPPRIOR'] = interim.number_of_new_world_ports_called_prior_to_disembarkation
    data['SLA1PORT'] = get_value(interim.first_place_of_landing)
    data['ADPSALE1'] = get_value(interim.second_place_of_landing)
    data['ADPSALE2'] = get_value(interim.third_place_of_landing)
    data['REGDIS1'] = get_region(interim.first_place_of_landing)
    data['REGDIS2'] = get_region(interim.second_place_of_landing)
    data['REGDIS3'] = get_region(interim.third_place_of_landing)
    data['PORTRET'] = get_value(interim.port_voyage_ended)
    data['RETRNREG'] = get_region(interim.port_voyage_ended)
    data['RETRNREG1'] = interim.port_voyage_ended.region.broad_region.value if interim.port_voyage_ended else None
    data['MAJBUYPT'] = get_value(interim.principal_place_of_slave_purchase)
    data['MAJSELPT'] = get_value(interim.principal_place_of_slave_disembarkation)

    # Imputed variables
    data['NATINIMP'] = interim.imputed_national_carrier
    data['TONMOD'] = interim.imputed_standardized_tonnage
    data['FATE2'] = interim.imputed_outcome_of_voyage_for_slaves
    data['FATE3'] = interim.imputed_outcome_of_voyage_if_ship_captured
    data['FATE4'] = interim.imputed_outcome_of_voyage_for_owner
    data['PTDEPIMP'] = interim.imputed_port_where_voyage_began
    data['MJBYPTIMP'] = interim.imputed_principal_place_of_slave_purchase
    data['MJSLPTIMP'] = interim.imputed_principal_port_of_slave_disembarkation
    data['DEPTREGIMP'] = interim.imputed_region_where_voyage_began
    data['REGDIS1'] = interim.imputed_first_region_of_slave_landing
    data['REGDIS2'] = interim.imputed_second_region_of_slave_landing
    data['REGDIS3'] = interim.imputed_third_region_of_slave_landing
    data['REGEM1'] = interim.imputed_first_region_of_embarkation_of_slaves
    data['REGEM2'] = interim.imputed_second_region_of_embarkation_of_slaves
    data['REGEM3'] = interim.imputed_third_region_of_embarkation_of_slaves
    data['YEARDEP'] = interim.imputed_year_voyage_began
    data['YEARAF'] = interim.imputed_year_departed_africa
    data['YEARAM'] = interim.imputed_year_arrived_at_port_of_disembarkation
    data['YEAR5'] = interim.imputed_quinquennium_in_which_voyage_occurred
    data['YEAR10'] = interim.imputed_decade_in_which_voyage_occurred
    data['YEAR25'] = interim.imputed_quarter_century_in_which_voyage_occurred
    data['YEAR100'] = interim.imputed_century_in_which_voyage_occurred
    data['VOY1IMP'] = interim.imputed_voyage_length_home_port_to_first_port_of_disembarkation
    data['VOY2IMP'] = interim.imputed_length_of_middle_passage
    data['XMIMPFLAG'] = interim.imputed_voyage_groupings_for_estimating_imputed_slaves
    data['SLAXIMP'] = interim.imputed_total_slaves_embarked
    data['SLAMIMP'] = interim.imputed_total_slaves_disembarked
    data['TSLMTIMP'] = interim.imputed_number_of_slaves_embarked_for_mortality_calculation
    data['VYMRTIMP'] = interim.imputed_total_slave_deaths_during_middle_passage
    data['VYMRTRAT'] = interim.imputed_mortality_rate
    data['JAMCASPR'] = interim.imputed_standardized_price_of_slaves
    
    # Sources
    created_sources = list(interim.article_sources.all()) + list(interim.book_sources.all()) + \
        list(interim.newspaper_sources.all()) + list(interim.private_note_or_collection_sources.all()) + \
        list(interim.unpublished_secondary_sources.all()) + list(interim.primary_sources.all())
    source_refs = [x.source_ref_text for x in created_sources] + \
        [x.full_ref for x in interim.pre_existing_sources.all()]
    aux = 'ABCDEFGHIJKLMNOPQR'
    for i, ref in enumerate(source_refs):
        data['SOURCE' + aux[i]] = ref
    
    # Numerical variables
    for n in interim.slave_numbers.all():
        data[n.var_name] = n.number
        
    return data

def _save_editorial_version(review_request, contrib_type):
    editor_contribution = review_request.editor_contribution.first()
    if editor_contribution is None or editor_contribution.interim_voyage is None:
        raise Exception('This type of contribution requires an editor review interim voyage for publication')
    interim = editor_contribution.interim_voyage
    # Create or load a voyage with the appropriate voyage id.
    voyage = Voyage()
    contrib = get_contribution_from_id(review_request.contribution_id)
    contrib.status = ContributionStatus.published
    contrib.save()
    if contrib_type == 'merge' or contrib_type == 'new':
        if not review_request.created_voyage_id:
            raise Exception('For new or merged contributions, an explicit voyage_id must be set')
        voyage.voyage_id = review_request.created_voyage_id
    elif contrib_type == 'edit':
        voyage = Voyage.objects.get(voyage_id=contrib.edited_voyage_id)
    else:
        raise Exception('Unsupported contribution type ' + contrib_type)
    # Edit field values and create child records for the voyage.
    if contrib_type != 'edit':
        voyage.voyage_in_cd_rom = False
    else:
        _delete_child_fk(voyage, 'voyage_ship')
        _delete_child_fk(voyage, 'voyage_itinerary')
        _delete_child_fk(voyage, 'voyage_dates')
        _delete_child_fk(voyage, 'voyage_crew')
        _delete_child_fk(voyage, 'voyage_slaves_numbers')
        voyage.voyage_captain.clear()
        voyage.voyage_ship_owner.clear()
        voyage.voyage_sources.clear()
    
    # Save voyage so that the database generates a primary key for it.
    voyage.voyage_groupings = interim.imputed_voyage_groupings_for_estimating_imputed_slaves
    voyage.save()
    
    def region(place):
        return None if place is None else place.region
        
    def broad_region(place):
        r = region(place)
        return None if r is None else r.broad_region
        
    # Voyage Ship
    ship = VoyageShip()
    ship.voyage = voyage
    ship.ship_name = interim.name_of_vessel
    ship.nationality_ship = interim.national_carrier
    ship.tonnage = interim.tonnage_of_vessel
    ship.ton_type = interim.ton_type
    ship.rig_of_vessel = interim.rig_of_vessel
    ship.guns_mounted = interim.guns_mounted
    ship.year_of_construction = interim.year_ship_constructed
    ship.vessel_construction_place = interim.ship_construction_place
    ship.vessel_construction_region = interim.imputed_region_ship_constructed
    ship.registered_year = interim.year_ship_registered
    ship.registered_place = interim.ship_registration_place
    ship.registered_region = region(interim.ship_registration_place)
    ship.imputed_nationality = interim.imputed_national_carrier
    ship.tonnage_mod = interim.imputed_standardized_tonnage
    ship.save()
    
    # Voyage Ship Owners
    def create_ship_owner(owner_name, order):
        owner = VoyageShipOwner()
        owner.name = owner_name
        owner.save()
        conn = VoyageShipOwnerConnection()
        conn.owner = owner
        conn.owner_order = order
        conn.voyage = voyage
        conn.save()
    
    if interim.first_ship_owner:
        create_ship_owner(interim.first_ship_owner, 1)
    if interim.second_ship_owner:
        create_ship_owner(interim.second_ship_owner, 2)
    if interim.additional_ship_owners:
        additional = interim.additional_ship_owners.split('\n')
        for index, owner in enumerate(additional):
            create_ship_owner(owner, index + 3)
            
    # Voyage Ship Captains
    def create_captain(name, order):
        captain = VoyageCaptain()
        captain.name = name
        captain.save()
        conn = VoyageCaptainConnection()
        conn.captain = captain
        conn.captain_order = order
        conn.voyage = voyage
        conn.save()
    
    if interim.first_captain:
        create_captain(interim.first_captain, 1)
    if interim.second_captain:
        create_captain(interim.second_captain, 2)
    if interim.third_captain:
        create_captain(interim.third_captain, 3)
    
    # Voyage Itinerary    
    itinerary = VoyageItinerary()
    itinerary.voyage = voyage
    itinerary.int_first_port_emb = interim.first_port_intended_embarkation
    itinerary.int_second_port_emb = interim.second_port_intended_embarkation
    itinerary.int_first_region_purchase_slaves = region(interim.first_port_intended_embarkation)
    itinerary.int_second_region_purchase_slaves = region(interim.second_port_intended_embarkation)
    itinerary.int_first_port_dis = interim.first_port_intended_disembarkation
    itinerary.int_second_port_dis = interim.second_port_intended_disembarkation
    itinerary.int_first_region_slave_landing = region(interim.first_port_intended_disembarkation)
    itinerary.int_second_place_region_slave_landing = region(interim.second_port_intended_disembarkation)
    itinerary.ports_called_buying_slaves = interim.number_of_ports_called_prior_to_slave_purchase
    itinerary.first_place_slave_purchase = interim.first_place_of_slave_purchase
    itinerary.second_place_slave_purchase = interim.second_place_of_slave_purchase
    itinerary.third_place_slave_purchase = interim.third_place_of_slave_purchase
    itinerary.first_region_slave_emb = region(interim.first_place_of_slave_purchase)
    itinerary.second_region_slave_emb = region(interim.second_place_of_slave_purchase)
    itinerary.third_region_slave_emb = region(interim.third_place_of_slave_purchase)
    itinerary.port_of_call_before_atl_crossing = interim.place_of_call_before_atlantic_crossing
    itinerary.number_of_ports_of_call = interim.number_of_new_world_ports_called_prior_to_disembarkation
    itinerary.first_landing_place = interim.first_place_of_landing
    itinerary.second_landing_place = interim.second_place_of_landing
    itinerary.third_landing_place = interim.third_place_of_landing
    itinerary.first_landing_region = region(interim.first_place_of_landing)
    itinerary.second_landing_region = region(interim.second_place_of_landing)
    itinerary.third_landing_region = region(interim.third_place_of_landing)
    itinerary.place_voyage_ended = interim.port_voyage_ended
    itinerary.region_of_return = region(interim.port_voyage_ended)
    itinerary.broad_region_of_return = broad_region(interim.port_voyage_ended)
    itinerary.imp_port_voyage_begin = interim.imputed_port_where_voyage_began
    itinerary.imp_region_voyage_begin = interim.imputed_region_where_voyage_began
    itinerary.imp_broad_region_voyage_begin = broad_region(interim.imputed_port_where_voyage_began)
    itinerary.principal_place_of_slave_purchase = interim.principal_place_of_slave_purchase
    itinerary.imp_principal_place_of_slave_purchase = interim.imputed_principal_place_of_slave_purchase
    itinerary.imp_principal_region_of_slave_purchase = region(interim.imputed_principal_place_of_slave_purchase)
    itinerary.imp_broad_region_of_slave_purchase = broad_region(interim.imputed_principal_place_of_slave_purchase)
    itinerary.principal_port_of_slave_dis = interim.principal_place_of_slave_disembarkation
    itinerary.imp_principal_port_slave_dis = interim.imputed_principal_port_of_slave_disembarkation
    itinerary.imp_principal_region_slave_dis = region(interim.imputed_principal_port_of_slave_disembarkation)
    itinerary.imp_broad_region_slave_dis = broad_region(interim.imputed_principal_port_of_slave_disembarkation)
    itinerary.save()
    
    # Voyage dates.
    def year_dummies(year):
        return ',,' + str(year)
    
    dates = VoyageDates()
    dates.voyage = voyage
    dates.voyage_began = interim.date_departure
    dates.slave_purchase_began = interim.date_slave_purchase_began
    dates.vessel_left_port = interim.date_vessel_left_last_slaving_port
    dates.first_dis_of_slaves = interim.date_first_slave_disembarkation
    #dates.date_departed_africa = interim.???  TODO: check this
    dates.arrival_at_second_place_landing = interim.date_second_slave_disembarkation
    dates.third_dis_of_slaves = interim.date_third_slave_disembarkation
    dates.departure_last_place_of_landing = interim.date_return_departure
    dates.voyage_completed = interim.date_voyage_completed
    dates.length_middle_passage_days = interim.length_of_middle_passage
    dates.imp_voyage_began = year_dummies(interim.imputed_year_voyage_began)
    dates.imp_departed_africa = year_dummies(interim.imputed_year_departed_africa)
    dates.imp_arrival_at_port_of_dis = year_dummies(interim.imputed_year_arrived_at_port_of_disembarkation)
    dates.imp_length_home_to_disembark = interim.imputed_voyage_length_home_port_to_first_port_of_disembarkation
    dates.imp_length_leaving_africa_to_disembark = interim.imputed_length_of_middle_passage
    dates.save()
    
    numbers = {n.var_name.upper(): n.number for n in interim.slave_numbers.all()}
    
    # Voyage crew
    crew = VoyageCrew()
    crew.voyage = voyage
    crew.crew_voyage_outset = numbers.get('CREW1')
    crew.crew_departure_last_port = numbers.get('CREW2')
    crew.crew_first_landing = numbers.get('CREW3')
    crew.crew_return_begin = numbers.get('CREW4')
    crew.crew_end_voyage = numbers.get('CREW5')
    crew.unspecified_crew = numbers.get('CREW')
    crew.crew_died_before_first_trade = numbers.get('SAILD1')
    crew.crew_died_while_ship_african = numbers.get('SAILD2')
    crew.crew_died_middle_passage = numbers.get('SAILD3')
    crew.crew_died_in_americas = numbers.get('SAILD4')
    crew.crew_died_on_return_voyage = numbers.get('SAILD5')
    crew.crew_died_complete_voyage = numbers.get('CREWDIED')
    crew.crew_deserted = numbers.get('NDESERT')
    crew.save()
    
    # Voyage slave numbers
    slaves_numbers = VoyageSlavesNumbers()
    slaves_numbers.voyage = voyage
    slaves_numbers.slave_deaths_before_africa = numbers.get('SLADAFRI')
    slaves_numbers.slave_deaths_between_africa_america = numbers.get('SLADVOY')
    slaves_numbers.slave_deaths_between_arrival_and_sale = numbers.get('SLADAMER')
    slaves_numbers.num_slaves_intended_first_port = numbers.get('SLINTEND')
    slaves_numbers.num_slaves_intended_second_port = numbers.get('SLINTEN2')
    slaves_numbers.num_slaves_carried_first_port = numbers.get('NCAR13')
    slaves_numbers.num_slaves_carried_second_port = numbers.get('NCAR15')
    slaves_numbers.num_slaves_carried_third_port = numbers.get('NCAR17')
    slaves_numbers.total_num_slaves_purchased = numbers.get('TSLAVESP')
    slaves_numbers.total_num_slaves_dep_last_slaving_port = numbers.get('TSLAVESD')
    slaves_numbers.total_num_slaves_arr_first_port_embark = numbers.get('SLAARRIV')
    slaves_numbers.num_slaves_disembark_first_place = numbers.get('SLAS32')
    slaves_numbers.num_slaves_disembark_second_place = numbers.get('SLAS36')
    slaves_numbers.num_slaves_disembark_third_place = numbers.get('SLAS39')
    slaves_numbers.imp_total_num_slaves_embarked = numbers.get('SLAXIMP')
    slaves_numbers.imp_total_num_slaves_disembarked = numbers.get('SLAMIMP')
    slaves_numbers.imp_jamaican_cash_price = numbers.get('JAMCASPR')
    slaves_numbers.imp_mortality_during_voyage = numbers.get('VYMRTIMP')
    slaves_numbers.num_men_embark_first_port_purchase = numbers.get('MEN1')
    slaves_numbers.num_women_embark_first_port_purchase = numbers.get('WOMEN1')
    slaves_numbers.num_boy_embark_first_port_purchase = numbers.get('BOY1')
    slaves_numbers.num_girl_embark_first_port_purchase = numbers.get('GIRL1')
    slaves_numbers.num_adult_embark_first_port_purchase = numbers.get('ADULT1')
    slaves_numbers.num_child_embark_first_port_purchase = numbers.get('CHILD1')
    slaves_numbers.num_infant_embark_first_port_purchase = numbers.get('INFANT1')
    slaves_numbers.num_males_embark_first_port_purchase = numbers.get('MALE1')
    slaves_numbers.num_females_embark_first_port_purchase = numbers.get('FEMALE1')
    slaves_numbers.num_men_died_middle_passage = numbers.get('MEN2')
    slaves_numbers.num_women_died_middle_passage = numbers.get('WOMEN2')
    slaves_numbers.num_boy_died_middle_passage = numbers.get('BOY2')
    slaves_numbers.num_girl_died_middle_passage = numbers.get('GIRL2')
    slaves_numbers.num_adult_died_middle_passage = numbers.get('ADULT2')
    slaves_numbers.num_child_died_middle_passage = numbers.get('CHILD2')
    slaves_numbers.num_infant_died_middle_passage = numbers.get('INFANT2')
    slaves_numbers.num_males_died_middle_passage = numbers.get('MALE2')
    slaves_numbers.num_females_died_middle_passage = numbers.get('FEMALE2')
    slaves_numbers.num_men_disembark_first_landing = numbers.get('MEN3')
    slaves_numbers.num_women_disembark_first_landing = numbers.get('WOMEN3')
    slaves_numbers.num_boy_disembark_first_landing = numbers.get('BOY3')
    slaves_numbers.num_girl_disembark_first_landing = numbers.get('GIRL3')
    slaves_numbers.num_adult_disembark_first_landing = numbers.get('ADULT3')
    slaves_numbers.num_child_disembark_first_landing = numbers.get('CHILD3')
    slaves_numbers.num_infant_disembark_first_landing = numbers.get('INFANT3')
    slaves_numbers.num_males_disembark_first_landing = numbers.get('MALE3')
    slaves_numbers.num_females_disembark_first_landing = numbers.get('FEMALE3')
    slaves_numbers.num_men_embark_second_port_purchase = numbers.get('MEN4')
    slaves_numbers.num_women_embark_second_port_purchase = numbers.get('WOMEN4')
    slaves_numbers.num_boy_embark_second_port_purchase = numbers.get('BOY4')
    slaves_numbers.num_girl_embark_second_port_purchase = numbers.get('GIRL4')
    slaves_numbers.num_adult_embark_second_port_purchase = numbers.get('ADULT4')
    slaves_numbers.num_child_embark_second_port_purchase = numbers.get('CHILD4')
    slaves_numbers.num_infant_embark_second_port_purchase = numbers.get('INFANT4')
    slaves_numbers.num_males_embark_second_port_purchase = numbers.get('MALE4')
    slaves_numbers.num_females_embark_second_port_purchase = numbers.get('FEMALE4')
    slaves_numbers.num_men_embark_third_port_purchase = numbers.get('MEN5')
    slaves_numbers.num_women_embark_third_port_purchase = numbers.get('WOMEN5')
    slaves_numbers.num_boy_embark_third_port_purchase = numbers.get('BOY5')
    slaves_numbers.num_girl_embark_third_port_purchase = numbers.get('GIRL5')
    slaves_numbers.num_adult_embark_third_port_purchase = numbers.get('ADULT5')
    slaves_numbers.num_child_embark_third_port_purchase = numbers.get('CHILD5')
    slaves_numbers.num_infant_embark_third_port_purchase = numbers.get('INFANT5')
    slaves_numbers.num_males_embark_third_port_purchase = numbers.get('MALE5')
    slaves_numbers.num_females_embark_third_port_purchase = numbers.get('FEMALE5')
    slaves_numbers.num_men_disembark_second_landing = numbers.get('MEN6')
    slaves_numbers.num_women_disembark_second_landing = numbers.get('WOMEN6')
    slaves_numbers.num_boy_disembark_second_landing = numbers.get('BOY6')
    slaves_numbers.num_girl_disembark_second_landing = numbers.get('GIRL6')
    slaves_numbers.num_adult_disembark_second_landing = numbers.get('ADULT6')
    slaves_numbers.num_child_disembark_second_landing = numbers.get('CHILD6')
    slaves_numbers.num_infant_disembark_second_landing = numbers.get('INFANT6')
    slaves_numbers.num_males_disembark_second_landing = numbers.get('MALE6')
    slaves_numbers.num_females_disembark_second_landing = numbers.get('FEMALE6')
    slaves_numbers.imp_num_adult_embarked = numbers.get('ADLT1IMP')
    slaves_numbers.imp_num_children_embarked = numbers.get('CHIL1IMP')
    slaves_numbers.imp_num_male_embarked = numbers.get('MALE1IMP')
    slaves_numbers.imp_num_female_embarked = numbers.get('FEML1IMP')
    slaves_numbers.total_slaves_embarked_age_identified = numbers.get('SLAVEMA1')
    slaves_numbers.total_slaves_embarked_gender_identified = numbers.get('SLAVEMX1')
    slaves_numbers.imp_adult_death_middle_passage = numbers.get('ADLT2IMP')
    slaves_numbers.imp_child_death_middle_passage = numbers.get('CHIL2IMP')
    slaves_numbers.imp_male_death_middle_passage = numbers.get('MALE2IMP')
    slaves_numbers.imp_female_death_middle_passage = numbers.get('FEML2IMP')
    slaves_numbers.imp_num_adult_landed = numbers.get('ADLT3IMP')
    slaves_numbers.imp_num_child_landed = numbers.get('CHIL3IMP')
    slaves_numbers.imp_num_male_landed = numbers.get('MALE3IMP')
    slaves_numbers.imp_num_female_landed = numbers.get('FEML3IMP')
    slaves_numbers.total_slaves_landed_age_identified = numbers.get('SLAVEMA3')
    slaves_numbers.total_slaves_landed_gender_identified = numbers.get('SLAVEMX3')
    slaves_numbers.total_slaves_dept_or_arr_age_identified = numbers.get('SLAVEMA7')
    slaves_numbers.total_slaves_dept_or_arr_gender_identified = numbers.get('SLAVEMX7')
    slaves_numbers.imp_slaves_embarked_for_mortality = numbers.get('TSLMTIMP')
    slaves_numbers.imp_num_men_total = numbers.get('MEN7')
    slaves_numbers.imp_num_women_total = numbers.get('WOMEN7')
    slaves_numbers.imp_num_boy_total = numbers.get('BOY7')
    slaves_numbers.imp_num_girl_total = numbers.get('GIRL7')
    slaves_numbers.imp_num_adult_total = numbers.get('ADULT7')
    slaves_numbers.imp_num_child_total = numbers.get('CHILD7')
    slaves_numbers.imp_num_males_total = numbers.get('MALE7')
    slaves_numbers.imp_num_females_total = numbers.get('FEMALE7')
    slaves_numbers.save()
    
    # Voyage sources
    def create_source_connection(src, conn_ref, order):
        conn = VoyageSourcesConnection()
        conn.source = src
        conn.group = voyage
        conn.source_order = order
        conn.text_ref = conn_ref
        conn.save()
    
    def create_source_reference(short_ref, conn_ref, order):
        src = VoyageSources.objects.filter(short_ref=short_ref).first()
        if src is None:
            raise Exception('Source "' + short_ref + '" not found')
        create_source_connection(src, conn_ref, order)
    
    created_sources = list(interim.article_sources.all()) + list(interim.book_sources.all()) + \
        list(interim.newspaper_sources.all()) + list(interim.private_note_or_collection_sources.all()) + \
        list(interim.unpublished_secondary_sources.all()) + list(interim.primary_sources.all())
    pre_existing_sources = list(interim.pre_existing_sources.all())
    if contrib_type != 'edit' and contrib_type != 'merge' and len(pre_existing_sources) > 0:
        raise Exception('A contribution with type "' + contrib_type + '" cannot have pre existing sources')
    source_order = 1 # TODO: ask Dr. Eltis to see how we should order references
    for src in created_sources:
        # Each src here has as type a subclass of InterimContributedSource
        if not src.created_voyage_sources:
            raise Exception('Invalid state: a new source must have been created to match "' + src.source_ref_text + '"')
        create_source_connection(src.created_voyage_sources, src.source_ref_text, source_order)
        source_order += 1
    for src in pre_existing_sources:
        if src.action == InterimPreExistingSourceActions.exclude: continue
        create_source_reference(src.original_short_ref, src.original_ref, source_order)
        source_order += 1
    
    # Set voyage foreign keys (this is redundant, but we are keeping the original model design)
    voyage.voyage_ship = ship
    voyage.voyage_itinerary = itinerary
    voyage.voyage_dates = dates
    voyage.voyage_crew = crew
    voyage.voyage_slaves_numbers = slaves_numbers
    voyage.save()
    
    return voyage
    
def _delete_voyages(ids):
    delete_voyages = list(Voyage.objects.filter(voyage_id__in=ids))
    if len(ids) != len(delete_voyages):
        raise Exception("Voyage not found for deletion, voyage ids=" + str(ids))
    for v in delete_voyages:
        v.delete()
    
def _publish_single_review_delete(review_request):
    contribution = get_contribution_from_id(review_request.contribution_id)
    ids = list(contribution.get_related_voyage_ids())
    _delete_voyages(ids)
    
def _publish_single_review_merge(review_request):
    contribution = get_contribution_from_id(review_request.contribution_id)
    # Delete previous records and create a new one to replace them.
    ids = list(contribution.get_related_voyage_ids())
    _delete_voyages(ids)
    _save_editorial_version(review_request, 'merge')
    
def _publish_single_review_new(review_request):
    _save_editorial_version(review_request, 'new')
    
def _publish_single_review_update(review_request):
    _save_editorial_version(review_request, 'edit')