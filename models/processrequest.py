#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ProcessRequest) on 2016-10-07.
#  2016, SMART Health IT.


from . import domainresource

class ProcessRequest(domainresource.DomainResource):
    """ Process request.
    
    This resource provides the target, request and response, and action details
    for an action to be performed by the target on or about existing resources.
    """
    
    resource_name = "ProcessRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None  #type: str
        """ cancel | poll | reprocess | status.
        Type `str`. """
        
        self.created = None  #type: fhirdate.FHIRDate
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.exclude = None  #type: str
        """ Resource type(s) to exclude.
        List of `str` items. """
        
        self.identifier = None  #type: identifier.Identifier
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.include = None  #type: str
        """ Resource type(s) to include.
        List of `str` items. """
        
        self.item = None  #type: ProcessRequestItem
        """ Items to re-adjudicate.
        List of `ProcessRequestItem` items (represented as `dict` in JSON). """
        
        self.nullify = None  #type: bool
        """ Nullify.
        Type `bool`. """
        
        self.organization = None  #type: fhirreference.FHIRReference
        """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.originalRuleset = None  #type: coding.Coding
        """ Original version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.period = None  #type: period.Period
        """ Period.
        Type `Period` (represented as `dict` in JSON). """
        
        self.provider = None  #type: fhirreference.FHIRReference
        """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.reference = None  #type: str
        """ Reference number/string.
        Type `str`. """
        
        self.request = None  #type: fhirreference.FHIRReference
        """ Request reference.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.response = None  #type: fhirreference.FHIRReference
        """ Response reference.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.ruleset = None  #type: coding.Coding
        """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.target = None  #type: fhirreference.FHIRReference
        """ Target of the request.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        super(ProcessRequest, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(ProcessRequest, self).elementProperties()
        js.extend([
            ("action", "action", str, False, None, True),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("exclude", "exclude", str, True, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("include", "include", str, True, None, False),
            ("item", "item", ProcessRequestItem, True, None, False),
            ("nullify", "nullify", bool, False, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("originalRuleset", "originalRuleset", coding.Coding, False, None, False),
            ("period", "period", period.Period, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("reference", "reference", str, False, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("response", "response", fhirreference.FHIRReference, False, None, False),
            ("ruleset", "ruleset", coding.Coding, False, None, False),
            ("target", "target", fhirreference.FHIRReference, False, None, False),
        ])
        return js


from . import backboneelement

class ProcessRequestItem(backboneelement.BackboneElement):
    """ Items to re-adjudicate.
    
    List of top level items to be re-adjudicated, if none specified then the
    entire submission is re-adjudicated.
    """
    
    resource_name = "ProcessRequestItem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.sequenceLinkId = None  #type: int
        """ Service instance.
        Type `int`. """
        
        super(ProcessRequestItem, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(ProcessRequestItem, self).elementProperties()
        js.extend([
            ("sequenceLinkId", "sequenceLinkId", int, False, None, True),
        ])
        return js


from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
