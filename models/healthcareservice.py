#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/HealthcareService) on 2016-10-07.
#  2016, SMART Health IT.


from . import domainresource

class HealthcareService(domainresource.DomainResource):
    """ The details of a healthcare service available at a location.
    """
    
    resource_name = "HealthcareService"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.appointmentRequired = None  #type: bool
        """ If an appointment is required for access to this service.
        Type `bool`. """
        
        self.availabilityExceptions = None  #type: str
        """ Description of availability exceptions.
        Type `str`. """
        
        self.availableTime = None  #type: HealthcareServiceAvailableTime
        """ Times the Service Site is available.
        List of `HealthcareServiceAvailableTime` items (represented as `dict` in JSON). """
        
        self.characteristic = None  #type: codeableconcept.CodeableConcept
        """ Collection of characteristics (attributes).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.comment = None  #type: str
        """ Additional description and/or any specific issues not covered
        elsewhere.
        Type `str`. """
        
        self.coverageArea = None  #type: fhirreference.FHIRReference
        """ Location(s) service is inteded for/available to.
        List of `FHIRReference` items referencing `Location` (represented as `dict` in JSON). """
        
        self.eligibility = None  #type: codeableconcept.CodeableConcept
        """ Specific eligibility requirements required to use the service.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.eligibilityNote = None  #type: str
        """ Describes the eligibility conditions for the service.
        Type `str`. """
        
        self.extraDetails = None  #type: str
        """ Extra details about the service that can't be placed in the other
        fields.
        Type `str`. """
        
        self.identifier = None  #type: identifier.Identifier
        """ External identifiers for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.location = None  #type: fhirreference.FHIRReference
        """ Location where service may be provided.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.notAvailable = None  #type: HealthcareServiceNotAvailable
        """ Not available during this time due to provided reason.
        List of `HealthcareServiceNotAvailable` items (represented as `dict` in JSON). """
        
        self.photo = None  #type: attachment.Attachment
        """ Facilitates quick identification of the service.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.programName = None  #type: str
        """ Program Names that categorize the service.
        List of `str` items. """
        
        self.providedBy = None  #type: fhirreference.FHIRReference
        """ Organization that provides this service.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.publicKey = None  #type: str
        """ PKI Public keys to support secure communications.
        Type `str`. """
        
        self.referralMethod = None  #type: codeableconcept.CodeableConcept
        """ Ways that the service accepts referrals.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.serviceCategory = None  #type: codeableconcept.CodeableConcept
        """ Broad category of service being performed or delivered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.serviceName = None  #type: str
        """ Description of service as presented to a consumer while searching.
        Type `str`. """
        
        self.serviceProvisionCode = None  #type: codeableconcept.CodeableConcept
        """ Conditions under which service is available/offered.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.serviceType = None  #type: HealthcareServiceServiceType
        """ Specific service delivered or performed.
        List of `HealthcareServiceServiceType` items (represented as `dict` in JSON). """
        
        self.telecom = None  #type: contactpoint.ContactPoint
        """ Contacts related to the healthcare service.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(HealthcareService, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(HealthcareService, self).elementProperties()
        js.extend([
            ("appointmentRequired", "appointmentRequired", bool, False, None, False),
            ("availabilityExceptions", "availabilityExceptions", str, False, None, False),
            ("availableTime", "availableTime", HealthcareServiceAvailableTime, True, None, False),
            ("characteristic", "characteristic", codeableconcept.CodeableConcept, True, None, False),
            ("comment", "comment", str, False, None, False),
            ("coverageArea", "coverageArea", fhirreference.FHIRReference, True, None, False),
            ("eligibility", "eligibility", codeableconcept.CodeableConcept, False, None, False),
            ("eligibilityNote", "eligibilityNote", str, False, None, False),
            ("extraDetails", "extraDetails", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, True),
            ("notAvailable", "notAvailable", HealthcareServiceNotAvailable, True, None, False),
            ("photo", "photo", attachment.Attachment, False, None, False),
            ("programName", "programName", str, True, None, False),
            ("providedBy", "providedBy", fhirreference.FHIRReference, False, None, False),
            ("publicKey", "publicKey", str, False, None, False),
            ("referralMethod", "referralMethod", codeableconcept.CodeableConcept, True, None, False),
            ("serviceCategory", "serviceCategory", codeableconcept.CodeableConcept, False, None, False),
            ("serviceName", "serviceName", str, False, None, False),
            ("serviceProvisionCode", "serviceProvisionCode", codeableconcept.CodeableConcept, True, None, False),
            ("serviceType", "serviceType", HealthcareServiceServiceType, True, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


from . import backboneelement

class HealthcareServiceAvailableTime(backboneelement.BackboneElement):
    """ Times the Service Site is available.
    
    A collection of times that the Service Site is available.
    """
    
    resource_name = "HealthcareServiceAvailableTime"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.allDay = None  #type: bool
        """ Always available? e.g. 24 hour service.
        Type `bool`. """
        
        self.availableEndTime = None  #type: fhirdate.FHIRDate
        """ Closing time of day (ignored if allDay = true).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.availableStartTime = None  #type: fhirdate.FHIRDate
        """ Opening time of day (ignored if allDay = true).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.daysOfWeek = None  #type: str
        """ mon | tue | wed | thu | fri | sat | sun.
        List of `str` items. """
        
        super(HealthcareServiceAvailableTime, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(HealthcareServiceAvailableTime, self).elementProperties()
        js.extend([
            ("allDay", "allDay", bool, False, None, False),
            ("availableEndTime", "availableEndTime", fhirdate.FHIRDate, False, None, False),
            ("availableStartTime", "availableStartTime", fhirdate.FHIRDate, False, None, False),
            ("daysOfWeek", "daysOfWeek", str, True, None, False),
        ])
        return js


class HealthcareServiceNotAvailable(backboneelement.BackboneElement):
    """ Not available during this time due to provided reason.
    
    The HealthcareService is not available during this period of time due to
    the provided reason.
    """
    
    resource_name = "HealthcareServiceNotAvailable"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None  #type: str
        """ Reason presented to the user explaining why time not available.
        Type `str`. """
        
        self.during = None  #type: period.Period
        """ Service not availablefrom this date.
        Type `Period` (represented as `dict` in JSON). """
        
        super(HealthcareServiceNotAvailable, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(HealthcareServiceNotAvailable, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, True),
            ("during", "during", period.Period, False, None, False),
        ])
        return js


class HealthcareServiceServiceType(backboneelement.BackboneElement):
    """ Specific service delivered or performed.
    
    A specific type of service that may be delivered or performed.
    """
    
    resource_name = "HealthcareServiceServiceType"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.specialty = None  #type: codeableconcept.CodeableConcept
        """ Specialties handled by the Service Site.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.type = None  #type: codeableconcept.CodeableConcept
        """ Type of service delivered or performed.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(HealthcareServiceServiceType, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(HealthcareServiceServiceType, self).elementProperties()
        js.extend([
            ("specialty", "specialty", codeableconcept.CodeableConcept, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, True),
        ])
        return js


from . import attachment
from . import codeableconcept
from . import contactpoint
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
