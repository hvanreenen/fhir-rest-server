#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/DeviceUseStatement) on 2016-10-07.
#  2016, SMART Health IT.


from . import domainresource

class DeviceUseStatement(domainresource.DomainResource):
    """ None.
    
    A record of a device being used by a patient where the record is the result
    of a report from the patient or another clinician.
    """
    
    resource_name = "DeviceUseStatement"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.bodySiteCodeableConcept = None  #type: codeableconcept.CodeableConcept
        """ Target body site.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.bodySiteReference = None  #type: fhirreference.FHIRReference
        """ Target body site.
        Type `FHIRReference` referencing `BodySite` (represented as `dict` in JSON). """
        
        self.device = None  #type: fhirreference.FHIRReference
        """ None.
        Type `FHIRReference` referencing `Device` (represented as `dict` in JSON). """
        
        self.identifier = None  #type: identifier.Identifier
        """ None.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.indication = None  #type: codeableconcept.CodeableConcept
        """ None.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.notes = None  #type: str
        """ None.
        List of `str` items. """
        
        self.recordedOn = None  #type: fhirdate.FHIRDate
        """ None.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.subject = None  #type: fhirreference.FHIRReference
        """ None.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.timingDateTime = None  #type: fhirdate.FHIRDate
        """ None.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.timingPeriod = None  #type: period.Period
        """ None.
        Type `Period` (represented as `dict` in JSON). """
        
        self.timingTiming = None  #type: timing.Timing
        """ None.
        Type `Timing` (represented as `dict` in JSON). """
        
        self.whenUsed = None  #type: period.Period
        """ None.
        Type `Period` (represented as `dict` in JSON). """
        
        super(DeviceUseStatement, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(DeviceUseStatement, self).elementProperties()
        js.extend([
            ("bodySiteCodeableConcept", "bodySiteCodeableConcept", codeableconcept.CodeableConcept, False, "bodySite", False),
            ("bodySiteReference", "bodySiteReference", fhirreference.FHIRReference, False, "bodySite", False),
            ("device", "device", fhirreference.FHIRReference, False, None, True),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("indication", "indication", codeableconcept.CodeableConcept, True, None, False),
            ("notes", "notes", str, True, None, False),
            ("recordedOn", "recordedOn", fhirdate.FHIRDate, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("timingDateTime", "timingDateTime", fhirdate.FHIRDate, False, "timing", False),
            ("timingPeriod", "timingPeriod", period.Period, False, "timing", False),
            ("timingTiming", "timingTiming", timing.Timing, False, "timing", False),
            ("whenUsed", "whenUsed", period.Period, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import timing
