#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/RiskAssessment) on 2016-10-07.
#  2016, SMART Health IT.


from . import domainresource

class RiskAssessment(domainresource.DomainResource):
    """ Potential outcomes for a subject with likelihood.
    
    An assessment of the likely outcome(s) for a patient or other subject as
    well as the likelihood of each outcome.
    """
    
    resource_name = "RiskAssessment"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.basis = None  #type: fhirreference.FHIRReference
        """ Information used in assessment.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        self.condition = None  #type: fhirreference.FHIRReference
        """ Condition assessed.
        Type `FHIRReference` referencing `Condition` (represented as `dict` in JSON). """
        
        self.date = None  #type: fhirdate.FHIRDate
        """ When was assessment made?.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.encounter = None  #type: fhirreference.FHIRReference
        """ Where was assessment performed?.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.identifier = None  #type: identifier.Identifier
        """ Unique identifier for the assessment.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.method = None  #type: codeableconcept.CodeableConcept
        """ Evaluation mechanism.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.mitigation = None  #type: str
        """ How to reduce risk.
        Type `str`. """
        
        self.performer = None  #type: fhirreference.FHIRReference
        """ Who did assessment?.
        Type `FHIRReference` referencing `Practitioner, Device` (represented as `dict` in JSON). """
        
        self.prediction = None  #type: RiskAssessmentPrediction
        """ Outcome predicted.
        List of `RiskAssessmentPrediction` items (represented as `dict` in JSON). """
        
        self.subject = None  #type: fhirreference.FHIRReference
        """ Who/what does assessment apply to?.
        Type `FHIRReference` referencing `Patient, Group` (represented as `dict` in JSON). """
        
        super(RiskAssessment, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(RiskAssessment, self).elementProperties()
        js.extend([
            ("basis", "basis", fhirreference.FHIRReference, True, None, False),
            ("condition", "condition", fhirreference.FHIRReference, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("method", "method", codeableconcept.CodeableConcept, False, None, False),
            ("mitigation", "mitigation", str, False, None, False),
            ("performer", "performer", fhirreference.FHIRReference, False, None, False),
            ("prediction", "prediction", RiskAssessmentPrediction, True, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
        ])
        return js


from . import backboneelement

class RiskAssessmentPrediction(backboneelement.BackboneElement):
    """ Outcome predicted.
    
    Describes the expected outcome for the subject.
    """
    
    resource_name = "RiskAssessmentPrediction"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.outcome = None  #type: codeableconcept.CodeableConcept
        """ Possible outcome for the subject.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.probabilityCodeableConcept = None  #type: codeableconcept.CodeableConcept
        """ Likelihood of specified outcome.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.probabilityDecimal = None  #type: float
        """ Likelihood of specified outcome.
        Type `float`. """
        
        self.probabilityRange = None  #type: range.Range
        """ Likelihood of specified outcome.
        Type `Range` (represented as `dict` in JSON). """
        
        self.rationale = None  #type: str
        """ Explanation of prediction.
        Type `str`. """
        
        self.relativeRisk = None  #type: float
        """ Relative likelihood.
        Type `float`. """
        
        self.whenPeriod = None  #type: period.Period
        """ Timeframe or age range.
        Type `Period` (represented as `dict` in JSON). """
        
        self.whenRange = None  #type: range.Range
        """ Timeframe or age range.
        Type `Range` (represented as `dict` in JSON). """
        
        super(RiskAssessmentPrediction, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(RiskAssessmentPrediction, self).elementProperties()
        js.extend([
            ("outcome", "outcome", codeableconcept.CodeableConcept, False, None, True),
            ("probabilityCodeableConcept", "probabilityCodeableConcept", codeableconcept.CodeableConcept, False, "probability", False),
            ("probabilityDecimal", "probabilityDecimal", float, False, "probability", False),
            ("probabilityRange", "probabilityRange", range.Range, False, "probability", False),
            ("rationale", "rationale", str, False, None, False),
            ("relativeRisk", "relativeRisk", float, False, None, False),
            ("whenPeriod", "whenPeriod", period.Period, False, "when", False),
            ("whenRange", "whenRange", range.Range, False, "when", False),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import range
