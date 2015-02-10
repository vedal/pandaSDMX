# encoding: utf-8

'''
.. module:: pandasdmx
    
    :synopsis: A Python- and pandas-powered client for statistical data and metadata exchange 
    For more details on SDMX see www.sdmx.org

.. :moduleauthor :: Dr. Leo fhaxbox66@gmail.com; forked from http://github.com/widukind/pysdmx
'''
  

from pandasdmx.application import app
from pandasdmx.request import Request

__all__ = ['Request']



def get(agency, resource, flow = None, key = None, params = {}):
    '''
    Convenience wrapper function initializing a pandasdmx.request.Request
    client and get an SDMX resource.
    '''
    r = Request(agency) 
    return r.get(resource, flow, key, params)

        