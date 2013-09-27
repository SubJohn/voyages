# -*- coding: utf-8 -*-

from django.test import TestCase
from django.test.utils import override_settings
from django.core.urlresolvers import reverse
import haystack
from mock import patch, Mock, MagicMock
from voyages.apps.help.models import Glossary, Faq
from voyages.apps.help.views import _sort_faq, _sort_glossary
from haystack.models import SearchResult


class TestGlossary(TestCase,):

    def setUp(self):

        glossary1 = {}
        glossary1['glossary_term_exact'] = 'Cats'
        glossary1['id'] = 'help.glossary.1'
        glossary1['app_label'] = 'help'
        glossary1['glossary_term'] = 'Cats'
        glossary1['pk'] =  '1'
        glossary1['model_name'] = 'glossary'
        glossary1['glossary_description'] = 'All about Cats'
        g1 = SearchResult('help', 'help.glossary', 1, None, _stored_fields = glossary1)


        glossary2 = {}
        glossary2['glossary_term_exact'] = 'Dogs'
        glossary2['id'] = 'help.glossary.2'
        glossary2['app_label'] = 'help'
        glossary2['glossary_term'] = 'Dogs'
        glossary2['pk'] =  '2'
        glossary2['model_name'] = 'glossary'
        glossary2['glossary_description'] = 'All about Dogs'
        g2 = SearchResult('help', 'help.glossary', 2, None, _stored_fields = glossary2)

        glossary3 = {}
        glossary3['glossary_term_exact'] = 'Anteaters'
        glossary3['id'] = 'help.glossary.3'
        glossary3['app_label'] = 'help'
        glossary3['glossary_term'] = 'Anteaters'
        glossary3['pk'] =  '3'
        glossary3['model_name'] = 'glossary'
        glossary3['glossary_description'] = 'All about Anteaters'
        g3 = SearchResult('help', 'help.glossary', 3, None, _stored_fields = glossary3)

        self.qresult =[g1, g2, g3]


    @patch('voyages.apps.help.views.SearchQuerySet')
    def test_search(self, mockquery):
        # GET initial page
        result = self.client.get(reverse('help:glossary'))
        self.assertEquals(result.status_code, 200)
        mockquery().models.assert_called_with(Glossary)
        mockquery().models(Glossary).order_by.assert_called_with('glossary_term_exact')


        # POST a query
        search = 'panda'
        result = self.client.post(reverse('help:glossary'), {'q' : search})
        self.assertEquals(result.status_code, 200)
        mockquery().filter.assert_called_with(content=search)
        mockquery().models.assert_called_with(Glossary)
        mockquery().filter(content=search).models(Glossary).order_by.assert_called_with('glossary_term_exact')

        # POST blank query
        search = ''
        result = self.client.post(reverse('help:glossary'), {'q' : search})
        self.assertEquals(result.status_code, 200)
        mockquery().filter.assert_called_with(content=search)
        mockquery().models.assert_called_with(Glossary)
        mockquery().filter(content=search).models(Glossary).order_by.assert_called_with('glossary_term_exact')


    def test_sort(self):
        letters, letters_found, glossary_content = _sort_glossary(self.qresult)
        expected_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                            'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.assertEquals(letters, expected_letters)

        self.assertEquals(letters_found['A'], 1)
        self.assertEquals(letters_found['B'], 0)
        self.assertEquals(letters_found['C'], 1)
        self.assertEquals(letters_found['D'], 1)

        self.assertEquals(glossary_content[0]['letter'], 'C')
        self.assertEquals(glossary_content[1]['letter'], 'D')
        self.assertEquals(glossary_content[2]['letter'], 'A')




class TestFaq(TestCase,):
    def setUp(self):

        faq1 = {}
        faq1['faq_category_desc'] = 'Bad Question'
        faq1['id'] = 'help.faq.1'
        faq1['app_label'] = 'help'
        faq1['pk'] =  '1'
        faq1['model_name'] = 'faq'
        faq1['faq_question'] = 'How old are you?'
        faq1['faq_answer'] = 'None of your business!'
        f1 = SearchResult('help', 'help.faq', 1, None, _stored_fields = faq1)


        faq2 = {}
        faq2['faq_category_desc'] = 'Bad Question'
        faq2['id'] = 'help.faq.2'
        faq2['app_label'] = 'help'
        faq2['pk'] =  '2'
        faq2['model_name'] = 'faq'
        faq2['faq_question'] = 'What is wrong with you?'
        faq2['faq_answer'] = '#$%@!'
        f2 = SearchResult('help', 'help.faq', 2, None, _stored_fields = faq2)

        faq3 = {}
        faq3['faq_category_desc'] = 'Good Question'
        faq3['id'] = 'help.faq.3'
        faq3['app_label'] = 'help'
        faq3['pk'] =  '3'
        faq3['model_name'] = 'faq'
        faq3['faq_question'] = 'What is for lunch?'
        faq3['faq_answer'] = 'Pizza!'
        f3 = SearchResult('help', 'help.faq', 3, None, _stored_fields = faq3)

        # real query will be sorted by category like these results
        self.qresult =[f1, f2, f3]

    @patch('voyages.apps.help.views.SearchQuerySet')
    def test_search(self, mockquery):
        # GET initial page
        result = self.client.get(reverse('help:faqs'))
        self.assertEquals(result.status_code, 200)
        mockquery().models.assert_called_with(Faq)
        mockquery().models(Faq).order_by.assert_called_with('faq_category_order', 'faq_question_order')



        # POST a query
        search = 'bear'
        result = self.client.post(reverse('help:faqs'), {'q' : search})
        self.assertEquals(result.status_code, 200)
        mockquery().filter.assert_called_with(content=search)
        mockquery().models.assert_called_with(Faq)
        mockquery().filter(content=search).models(Faq).order_by.assert_called_with('faq_category_order', 'faq_question_order')

        # POST blank query
        search = ''
        result = self.client.post(reverse('help:faqs'), {'q' : search})
        self.assertEquals(result.status_code, 200)
        mockquery().filter.assert_called_with(content=search)
        mockquery().models.assert_called_with(Faq)
        mockquery().filter(content=search).models(Faq).order_by.assert_called_with('faq_category_order', 'faq_question_order')

    def test_sort(self):
        faq_list = _sort_faq(self.qresult)
        
        self.assertEqual(len(faq_list), 2)
        self.assertEqual(len(faq_list[0]['questions']), 2)
        self.assertEqual(len(faq_list[1]['questions']), 1)

