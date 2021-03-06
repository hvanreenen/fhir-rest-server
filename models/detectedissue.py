#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/DetectedIssue) on 2016-10-07.
#  2016, SMART Health IT.


from . import domainresource

class DetectedIssue(domainresource.DomainResource):
    """ Clinical issue with action.
    
    Indicates an actual or potential clinical issue with or between one or more
    active or proposed clinical actions for a patient; e.g. Drug-drug
    interaction, Ineffective treatment frequency, Procedure-condition conflict,
    etc.
    """
    
    resource_name = "DetectedIssue"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.author = None  #type: fhirreference.FHIRReference
        """ The provider or device that identified the issue.
        Type `FHIRReference` referencing `Practitioner, Device` (represented as `dict` in JSON). """
        
        self.category = None  #type: codeableconcept.CodeableConcept
        """ Issue Category, e.g. drug-drug, duplicate therapy, etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.date = None  #type: fhirdate.FHIRDate
        """ When identified.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.detail = None  #type: str
        """ Description and context.
        Type `str`. """
        
        self.identifier = None  #type: identifier.Identifier
        """ Unique id for the detected issue.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.implicated = None  #type: fhirreference.FHIRReference
        """ Problem resource.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        self.mitigation = None  #type: DetectedIssueMitigation
        """ Step taken to address.
        List of `DetectedIssueMitigation` items (represented as `dict` in JSON). """
        
        self.patient = None  #type: fhirreference.FHIRReference
        """ Associated patient.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.reference = None  #type: str
        """ Authority for issue.
        Type `str`. """
        
        self.severity = None  #type: str
        """ high | moderate | low.
        Type `str`. """
        
        super(DetectedIssue, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(DetectedIssue, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("detail", "detail", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("implicated", "implicated", fhirreference.FHIRReference, True, None, False),
            ("mitigation", "mitigation", DetectedIssueMitigation, True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("reference", "reference", str, False, None, False),
            ("severity", "severity", str, False, None, False),
        ])
        return js


from . import backboneelement

class DetectedIssueMitigation(backboneelement.BackboneElement):
    """ Step taken to address.
    
    Indicates an action that has been taken or is committed to to reduce or
    eliminate the likelihood of the risk identified by the detected issue from
    manifesting.  Can also reflect an observation of known mitigating factors
    that may reduce/eliminate the need for any action.
    """
    
    resource_name = "DetectedIssueMitigation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None  #type: codeableconcept.CodeableConcept
        """ What mitigation?.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.author = None  #type: fhirreference.FHIRReference
        """ Who is committing?.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.date = None  #type: fhirdate.FHIRDate
        """ Date committed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(DetectedIssueMitigation, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(DetectedIssueMitigation, self).elementProperties()
        js.extend([
            ("action", "action", codeableconcept.CodeableConcept, False, None, True),
            ("author", "author", fhirreference.FHIRReference, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
