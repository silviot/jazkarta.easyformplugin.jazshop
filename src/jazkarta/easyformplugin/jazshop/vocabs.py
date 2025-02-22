from plone import api
from jazkarta.shop.interfaces import IProduct
from zope.interface import directlyProvides
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
from Products.CMFPlone.utils import safe_unicode


def get_available_products_vocab(context):
    terms = []
    catalog = api.portal.get_tool('portal_catalog')
    products = catalog(
        object_provides=IProduct.__identifier__,
        sort_on='sortable_title',
        sort_order='ascending')
    for product in products:
        terms.append(SimpleTerm(
            value=safe_unicode(product.UID),
            token=product.UID,
            title=product.Title,
        ))
    return SimpleVocabulary(terms)
directlyProvides(get_available_products_vocab, IVocabularyFactory)
