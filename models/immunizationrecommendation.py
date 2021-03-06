#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ImmunizationRecommendation) on 2016-10-07.
#  2016, SMART Health IT.


from . import domainresource

class ImmunizationRecommendation(domainresource.DomainResource):
    """ Guidance or advice relating to an immunization.
    
    A patient's point-in-time immunization and recommendation (i.e. forecasting
    a patient's immunization eligibility according to a published schedule)
    with optional supporting justification.
    """
    
    resource_name = "ImmunizationRecommendation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None  #type: identifier.Identifier
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.patient = None  #type: fhirreference.FHIRReference
        """ Who this profile is for.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.recommendation = None  #type: ImmunizationRecommendationRecommendation
        """ Vaccine administration recommendations.
        List of `ImmunizationRecommendationRecommendation` items (represented as `dict` in JSON). """
        
        super(ImmunizationRecommendation, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(ImmunizationRecommendation, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, True),
            ("recommendation", "recommendation", ImmunizationRecommendationRecommendation, True, None, True),
        ])
        return js


from . import backboneelement

class ImmunizationRecommendationRecommendation(backboneelement.BackboneElement):
    """ Vaccine administration recommendations.
    """
    
    resource_name = "ImmunizationRecommendationRecommendation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date = None  #type: fhirdate.FHIRDate
        """ Date recommendation created.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.dateCriterion = None  #type: ImmunizationRecommendationRecommendationDateCriterion
        """ Dates governing proposed immunization.
        List of `ImmunizationRecommendationRecommendationDateCriterion` items (represented as `dict` in JSON). """
        
        self.doseNumber = None  #type: int
        """ Recommended dose number.
        Type `int`. """
        
        self.forecastStatus = None  #type: codeableconcept.CodeableConcept
        """ Vaccine administration status.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.protocol = None  #type: ImmunizationRecommendationRecommendationProtocol
        """ Protocol used by recommendation.
        Type `ImmunizationRecommendationRecommendationProtocol` (represented as `dict` in JSON). """
        
        self.supportingImmunization = None  #type: fhirreference.FHIRReference
        """ Past immunizations supporting recommendation.
        List of `FHIRReference` items referencing `Immunization` (represented as `dict` in JSON). """
        
        self.supportingPatientInformation = None  #type: fhirreference.FHIRReference
        """ Patient observations supporting recommendation.
        List of `FHIRReference` items referencing `Observation, AllergyIntolerance` (represented as `dict` in JSON). """
        
        self.vaccineCode = None  #type: codeableconcept.CodeableConcept
        """ Vaccine recommendation applies to.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ImmunizationRecommendationRecommendation, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(ImmunizationRecommendationRecommendation, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, True),
            ("dateCriterion", "dateCriterion", ImmunizationRecommendationRecommendationDateCriterion, True, None, False),
            ("doseNumber", "doseNumber", int, False, None, False),
            ("forecastStatus", "forecastStatus", codeableconcept.CodeableConcept, False, None, True),
            ("protocol", "protocol", ImmunizationRecommendationRecommendationProtocol, False, None, False),
            ("supportingImmunization", "supportingImmunization", fhirreference.FHIRReference, True, None, False),
            ("supportingPatientInformation", "supportingPatientInformation", fhirreference.FHIRReference, True, None, False),
            ("vaccineCode", "vaccineCode", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


class ImmunizationRecommendationRecommendationDateCriterion(backboneelement.BackboneElement):
    """ Dates governing proposed immunization.
    
    Vaccine date recommendations.  For example, earliest date to administer,
    latest date to administer, etc.
    """
    
    resource_name = "ImmunizationRecommendationRecommendationDateCriterion"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None  #type: codeableconcept.CodeableConcept
        """ Type of date.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.value = None  #type: fhirdate.FHIRDate
        """ Recommended date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(ImmunizationRecommendationRecommendationDateCriterion, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(ImmunizationRecommendationRecommendationDateCriterion, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("value", "value", fhirdate.FHIRDate, False, None, True),
        ])
        return js


class ImmunizationRecommendationRecommendationProtocol(backboneelement.BackboneElement):
    """ Protocol used by recommendation.
    
    Contains information about the protocol under which the vaccine was
    administered.
    """
    
    resource_name = "ImmunizationRecommendationRecommendationProtocol"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.authority = None  #type: fhirreference.FHIRReference
        """ Who is responsible for protocol.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.description = None  #type: str
        """ Protocol details.
        Type `str`. """
        
        self.doseSequence = None  #type: int
        """ Dose number within sequence.
        Type `int`. """
        
        self.series = None  #type: str
        """ Name of vaccination series.
        Type `str`. """
        
        super(ImmunizationRecommendationRecommendationProtocol, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(ImmunizationRecommendationRecommendationProtocol, self).elementProperties()
        js.extend([
            ("authority", "authority", fhirreference.FHIRReference, False, None, False),
            ("description", "description", str, False, None, False),
            ("doseSequence", "doseSequence", int, False, None, False),
            ("series", "series", str, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
