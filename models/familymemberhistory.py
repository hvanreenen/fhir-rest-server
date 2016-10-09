#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/FamilyMemberHistory) on 2016-10-07.
#  2016, SMART Health IT.


from . import domainresource

class FamilyMemberHistory(domainresource.DomainResource):
    """ Information about patient's relatives, relevant for patient.
    
    Significant health events and conditions for a person related to the
    patient relevant in the context of care for the patient.
    """
    
    resource_name = "FamilyMemberHistory"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.ageQuantity = None  #type: quantity.Quantity
        """ (approximate) age.
        Type `Quantity` referencing `Age` (represented as `dict` in JSON). """
        
        self.ageRange = None  #type: range.Range
        """ (approximate) age.
        Type `Range` (represented as `dict` in JSON). """
        
        self.ageString = None  #type: str
        """ (approximate) age.
        Type `str`. """
        
        self.bornDate = None  #type: fhirdate.FHIRDate
        """ (approximate) date of birth.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.bornPeriod = None  #type: period.Period
        """ (approximate) date of birth.
        Type `Period` (represented as `dict` in JSON). """
        
        self.bornString = None  #type: str
        """ (approximate) date of birth.
        Type `str`. """
        
        self.condition = None  #type: FamilyMemberHistoryCondition
        """ Condition that the related person had.
        List of `FamilyMemberHistoryCondition` items (represented as `dict` in JSON). """
        
        self.date = None  #type: fhirdate.FHIRDate
        """ When history was captured/updated.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.deceasedBoolean = None  #type: bool
        """ Dead? How old/when?.
        Type `bool`. """
        
        self.deceasedDate = None  #type: fhirdate.FHIRDate
        """ Dead? How old/when?.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.deceasedQuantity = None  #type: quantity.Quantity
        """ Dead? How old/when?.
        Type `Quantity` referencing `Age` (represented as `dict` in JSON). """
        
        self.deceasedRange = None  #type: range.Range
        """ Dead? How old/when?.
        Type `Range` (represented as `dict` in JSON). """
        
        self.deceasedString = None  #type: str
        """ Dead? How old/when?.
        Type `str`. """
        
        self.gender = None  #type: str
        """ male | female | other | unknown.
        Type `str`. """
        
        self.identifier = None  #type: identifier.Identifier
        """ External Id(s) for this record.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.name = None  #type: str
        """ The family member described.
        Type `str`. """
        
        self.note = None  #type: annotation.Annotation
        """ General note about related person.
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.patient = None  #type: fhirreference.FHIRReference
        """ Patient history is about.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.relationship = None  #type: codeableconcept.CodeableConcept
        """ Relationship to the subject.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.status = None  #type: str
        """ partial | completed | entered-in-error | health-unknown.
        Type `str`. """
        
        super(FamilyMemberHistory, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(FamilyMemberHistory, self).elementProperties()
        js.extend([
            ("ageQuantity", "ageQuantity", quantity.Quantity, False, "age", False),
            ("ageRange", "ageRange", range.Range, False, "age", False),
            ("ageString", "ageString", str, False, "age", False),
            ("bornDate", "bornDate", fhirdate.FHIRDate, False, "born", False),
            ("bornPeriod", "bornPeriod", period.Period, False, "born", False),
            ("bornString", "bornString", str, False, "born", False),
            ("condition", "condition", FamilyMemberHistoryCondition, True, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("deceasedBoolean", "deceasedBoolean", bool, False, "deceased", False),
            ("deceasedDate", "deceasedDate", fhirdate.FHIRDate, False, "deceased", False),
            ("deceasedQuantity", "deceasedQuantity", quantity.Quantity, False, "deceased", False),
            ("deceasedRange", "deceasedRange", range.Range, False, "deceased", False),
            ("deceasedString", "deceasedString", str, False, "deceased", False),
            ("gender", "gender", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("name", "name", str, False, None, False),
            ("note", "note", annotation.Annotation, False, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("relationship", "relationship", codeableconcept.CodeableConcept, False, None, True),
            ("status", "status", str, False, None, True),
        ])
        return js


from . import backboneelement

class FamilyMemberHistoryCondition(backboneelement.BackboneElement):
    """ Condition that the related person had.
    
    The significant Conditions (or condition) that the family member had. This
    is a repeating section to allow a system to represent more than one
    condition per resource, though there is nothing stopping multiple resources
    - one per condition.
    """
    
    resource_name = "FamilyMemberHistoryCondition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None  #type: codeableconcept.CodeableConcept
        """ Condition suffered by relation.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.note = None  #type: annotation.Annotation
        """ Extra information about condition.
        Type `Annotation` (represented as `dict` in JSON). """
        
        self.onsetPeriod = None  #type: period.Period
        """ When condition first manifested.
        Type `Period` (represented as `dict` in JSON). """
        
        self.onsetQuantity = None  #type: quantity.Quantity
        """ When condition first manifested.
        Type `Quantity` referencing `Age` (represented as `dict` in JSON). """
        
        self.onsetRange = None  #type: range.Range
        """ When condition first manifested.
        Type `Range` (represented as `dict` in JSON). """
        
        self.onsetString = None  #type: str
        """ When condition first manifested.
        Type `str`. """
        
        self.outcome = None  #type: codeableconcept.CodeableConcept
        """ deceased | permanent disability | etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(FamilyMemberHistoryCondition, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(FamilyMemberHistoryCondition, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("note", "note", annotation.Annotation, False, None, False),
            ("onsetPeriod", "onsetPeriod", period.Period, False, "onset", False),
            ("onsetQuantity", "onsetQuantity", quantity.Quantity, False, "onset", False),
            ("onsetRange", "onsetRange", range.Range, False, "onset", False),
            ("onsetString", "onsetString", str, False, "onset", False),
            ("outcome", "outcome", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import annotation
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import quantity
from . import range
