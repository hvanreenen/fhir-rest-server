#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/EnrollmentRequest) on 2016-10-07.
#  2016, SMART Health IT.


from . import domainresource

class EnrollmentRequest(domainresource.DomainResource):
    """ Enrollment request.
    
    This resource provides the insurance enrollment details to the insurer
    regarding a specified coverage.
    """
    
    resource_name = "EnrollmentRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.coverage = None  #type: fhirreference.FHIRReference
        """ Insurance information.
        Type `FHIRReference` referencing `Coverage` (represented as `dict` in JSON). """
        
        self.created = None  #type: fhirdate.FHIRDate
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier = None  #type: identifier.Identifier
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.organization = None  #type: fhirreference.FHIRReference
        """ Responsible organization.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.originalRuleset = None  #type: coding.Coding
        """ Original version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.provider = None  #type: fhirreference.FHIRReference
        """ Responsible practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.relationship = None  #type: coding.Coding
        """ Patient relationship to subscriber.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.ruleset = None  #type: coding.Coding
        """ Resource version.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.subject = None  #type: fhirreference.FHIRReference
        """ The subject of the Products and Services.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.target = None  #type: fhirreference.FHIRReference
        """ Insurer.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        super(EnrollmentRequest, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(EnrollmentRequest, self).elementProperties()
        js.extend([
            ("coverage", "coverage", fhirreference.FHIRReference, False, None, True),
            ("created", "created", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("organization", "organization", fhirreference.FHIRReference, False, None, False),
            ("originalRuleset", "originalRuleset", coding.Coding, False, None, False),
            ("provider", "provider", fhirreference.FHIRReference, False, None, False),
            ("relationship", "relationship", coding.Coding, False, None, True),
            ("ruleset", "ruleset", coding.Coding, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("target", "target", fhirreference.FHIRReference, False, None, False),
        ])
        return js


from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
