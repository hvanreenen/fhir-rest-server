#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/DeviceUseRequest) on 2016-10-07.
#  2016, SMART Health IT.


from . import domainresource

class DeviceUseRequest(domainresource.DomainResource):
    """ A request for a patient to use or be given a medical device.
    
    Represents a request for a patient to employ a medical device. The device
    may be an implantable device, or an external assistive device, such as a
    walker.
    """
    
    resource_name = "DeviceUseRequest"
    
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
        """ Device requested.
        Type `FHIRReference` referencing `Device` (represented as `dict` in JSON). """
        
        self.encounter = None  #type: fhirreference.FHIRReference
        """ Encounter motivating request.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.identifier = None  #type: identifier.Identifier
        """ Request identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.indication = None  #type: codeableconcept.CodeableConcept
        """ Reason for request.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.notes = None  #type: str
        """ Notes or comments.
        List of `str` items. """
        
        self.orderedOn = None  #type: fhirdate.FHIRDate
        """ When ordered.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.priority = None  #type: str
        """ routine | urgent | stat | asap.
        Type `str`. """
        
        self.prnReason = None  #type: codeableconcept.CodeableConcept
        """ PRN.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.recordedOn = None  #type: fhirdate.FHIRDate
        """ When recorded.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.status = None  #type: str
        """ proposed | planned | requested | received | accepted | in-progress
        | completed | suspended | rejected | aborted.
        Type `str`. """
        
        self.subject = None  #type: fhirreference.FHIRReference
        """ Focus of request.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.timingDateTime = None  #type: fhirdate.FHIRDate
        """ Schedule for use.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.timingPeriod = None  #type: period.Period
        """ Schedule for use.
        Type `Period` (represented as `dict` in JSON). """
        
        self.timingTiming = None  #type: timing.Timing
        """ Schedule for use.
        Type `Timing` (represented as `dict` in JSON). """
        
        super(DeviceUseRequest, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(DeviceUseRequest, self).elementProperties()
        js.extend([
            ("bodySiteCodeableConcept", "bodySiteCodeableConcept", codeableconcept.CodeableConcept, False, "bodySite", False),
            ("bodySiteReference", "bodySiteReference", fhirreference.FHIRReference, False, "bodySite", False),
            ("device", "device", fhirreference.FHIRReference, False, None, True),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("indication", "indication", codeableconcept.CodeableConcept, True, None, False),
            ("notes", "notes", str, True, None, False),
            ("orderedOn", "orderedOn", fhirdate.FHIRDate, False, None, False),
            ("priority", "priority", str, False, None, False),
            ("prnReason", "prnReason", codeableconcept.CodeableConcept, True, None, False),
            ("recordedOn", "recordedOn", fhirdate.FHIRDate, False, None, False),
            ("status", "status", str, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, True),
            ("timingDateTime", "timingDateTime", fhirdate.FHIRDate, False, "timing", False),
            ("timingPeriod", "timingPeriod", period.Period, False, "timing", False),
            ("timingTiming", "timingTiming", timing.Timing, False, "timing", False),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
from . import timing
