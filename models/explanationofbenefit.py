#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ExplanationOfBenefit) on 2016-10-07.
#  2016, SMART Health IT.


from . import domainresource

class ExplanationOfBenefit(domainresource.DomainResource):
    """ Remittance resource.
    
    This resource provides: the claim details; adjudication details from the
    processing of a Claim; and optionally account balance information, for
    informing the subscriber of the benefits provided.
    """
    
    resource_name = "ExplanationOfBenefit"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.created = None  #type: fhirdate.FHIRDate
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.disposition = None  #type: str
        """ Disposition Message.
        Type `str`. """
        
        self.identifier = None  #type: identifier.Identifier
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.organization = None  #type: fhirreference.FHIRReference
        """ Insurer.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.originalRuleset = None  #type: coding.Coding
        """ Original version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.outcome = None  #type: str
        """ complete | error.
        Type `str`. """
        
        self.request = None  #type: fhirreference.FHIRReference
        """ Claim reference.
        Type `FHIRReference` referencing `Claim` (represented as `dict` in JSON). """
        
        self.requestOrganization = None  #type: fhirreference.FHIRReference
        """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.requestProvider = None  #type: fhirreference.FHIRReference
        """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.ruleset = None  #type: coding.Coding
        """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ExplanationOfBenefit, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(ExplanationOfBenefit, self).elementProperties()
        js.extend([
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("disposition", "disposition", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("originalRuleset", "originalRuleset", coding.Coding, False, None, False),
            ("outcome", "outcome", str, False, None, False),
            ("request", "request", fhirreference.FHIRReference, False, None, False),
            ("requestOrganization", "requestOrganization", fhirreference.FHIRReference, False, None, False),
            ("requestProvider", "requestProvider", fhirreference.FHIRReference, False, None, False),
            ("ruleset", "ruleset", coding.Coding, False, None, False),
        ])
        return js


from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
