#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/AuditEvent) on 2016-10-07.
#  2016, SMART Health IT.


from . import domainresource

class AuditEvent(domainresource.DomainResource):
    """ Event record kept for security purposes.
    
    A record of an event made for purposes of maintaining a security log.
    Typical uses include detection of intrusion attempts and monitoring for
    inappropriate usage.
    """
    
    resource_name = "AuditEvent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.event = None  #type: AuditEventEvent
        """ What was done.
        Type `AuditEventEvent` (represented as `dict` in JSON). """
        
        self.object = None  #type: AuditEventObject
        """ Specific instances of data or objects that have been accessed.
        List of `AuditEventObject` items (represented as `dict` in JSON). """
        
        self.participant = None  #type: AuditEventParticipant
        """ A person, a hardware device or software process.
        List of `AuditEventParticipant` items (represented as `dict` in JSON). """
        
        self.source = None  #type: AuditEventSource
        """ Application systems and processes.
        Type `AuditEventSource` (represented as `dict` in JSON). """
        
        super(AuditEvent, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(AuditEvent, self).elementProperties()
        js.extend([
            ("event", "event", AuditEventEvent, False, None, True),
            ("object", "object", AuditEventObject, True, None, False),
            ("participant", "participant", AuditEventParticipant, True, None, True),
            ("source", "source", AuditEventSource, False, None, True),
        ])
        return js


from . import backboneelement

class AuditEventEvent(backboneelement.BackboneElement):
    """ What was done.
    
    Identifies the name, action type, time, and disposition of the audited
    event.
    """
    
    resource_name = "AuditEventEvent"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.action = None  #type: str
        """ Type of action performed during the event.
        Type `str`. """
        
        self.dateTime = None  #type: fhirdate.FHIRDate
        """ Time when the event occurred on source.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.outcome = None  #type: str
        """ Whether the event succeeded or failed.
        Type `str`. """
        
        self.outcomeDesc = None  #type: str
        """ Description of the event outcome.
        Type `str`. """
        
        self.purposeOfEvent = None  #type: coding.Coding
        """ The purposeOfUse of the event.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.subtype = None  #type: coding.Coding
        """ More specific type/id for the event.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.type = None  #type: coding.Coding
        """ Type/identifier of event.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(AuditEventEvent, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(AuditEventEvent, self).elementProperties()
        js.extend([
            ("action", "action", str, False, None, False),
            ("dateTime", "dateTime", fhirdate.FHIRDate, False, None, True),
            ("outcome", "outcome", str, False, None, False),
            ("outcomeDesc", "outcomeDesc", str, False, None, False),
            ("purposeOfEvent", "purposeOfEvent", coding.Coding, True, None, False),
            ("subtype", "subtype", coding.Coding, True, None, False),
            ("type", "type", coding.Coding, False, None, True),
        ])
        return js


class AuditEventObject(backboneelement.BackboneElement):
    """ Specific instances of data or objects that have been accessed.
    """
    
    resource_name = "AuditEventObject"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.description = None  #type: str
        """ Descriptive text.
        Type `str`. """
        
        self.detail = None  #type: AuditEventObjectDetail
        """ Additional Information about the Object.
        List of `AuditEventObjectDetail` items (represented as `dict` in JSON). """
        
        self.identifier = None  #type: identifier.Identifier
        """ Specific instance of object (e.g. versioned).
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.lifecycle = None  #type: coding.Coding
        """ Life-cycle stage for the object.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.name = None  #type: str
        """ Instance-specific descriptor for Object.
        Type `str`. """
        
        self.query = None  #type: str
        """ Actual query for object.
        Type `str`. """
        
        self.reference = None  #type: fhirreference.FHIRReference
        """ Specific instance of resource (e.g. versioned).
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.role = None  #type: coding.Coding
        """ What role the Object played.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.securityLabel = None  #type: coding.Coding
        """ Security labels applied to the object.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.type = None  #type: coding.Coding
        """ Type of object involved.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(AuditEventObject, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(AuditEventObject, self).elementProperties()
        js.extend([
            ("description", "description", str, False, None, False),
            ("detail", "detail", AuditEventObjectDetail, True, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("lifecycle", "lifecycle", coding.Coding, False, None, False),
            ("name", "name", str, False, None, False),
            ("query", "query", str, False, None, False),
            ("reference", "reference", fhirreference.FHIRReference, False, None, False),
            ("role", "role", coding.Coding, False, None, False),
            ("securityLabel", "securityLabel", coding.Coding, True, None, False),
            ("type", "type", coding.Coding, False, None, False),
        ])
        return js


class AuditEventObjectDetail(backboneelement.BackboneElement):
    """ Additional Information about the Object.
    """
    
    resource_name = "AuditEventObjectDetail"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.type = None  #type: str
        """ Name of the property.
        Type `str`. """
        
        self.value = None  #type: str
        """ Property value.
        Type `str`. """
        
        super(AuditEventObjectDetail, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(AuditEventObjectDetail, self).elementProperties()
        js.extend([
            ("type", "type", str, False, None, True),
            ("value", "value", str, False, None, True),
        ])
        return js


class AuditEventParticipant(backboneelement.BackboneElement):
    """ A person, a hardware device or software process.
    """
    
    resource_name = "AuditEventParticipant"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.altId = None  #type: str
        """ Alternative User id e.g. authentication.
        Type `str`. """
        
        self.location = None  #type: fhirreference.FHIRReference
        """ Where.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.media = None  #type: coding.Coding
        """ Type of media.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.name = None  #type: str
        """ Human-meaningful name for the user.
        Type `str`. """
        
        self.network = None  #type: AuditEventParticipantNetwork
        """ Logical network location for application activity.
        Type `AuditEventParticipantNetwork` (represented as `dict` in JSON). """
        
        self.policy = None  #type: str
        """ Policy that authorized event.
        List of `str` items. """
        
        self.purposeOfUse = None  #type: coding.Coding
        """ Reason given for this user.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.reference = None  #type: fhirreference.FHIRReference
        """ Direct reference to resource.
        Type `FHIRReference` referencing `Practitioner, Organization, Device, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.requestor = None  #type: bool
        """ Whether user is initiator.
        Type `bool`. """
        
        self.role = None  #type: codeableconcept.CodeableConcept
        """ User roles (e.g. local RBAC codes).
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.userId = None  #type: identifier.Identifier
        """ Unique identifier for the user.
        Type `Identifier` (represented as `dict` in JSON). """
        
        super(AuditEventParticipant, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(AuditEventParticipant, self).elementProperties()
        js.extend([
            ("altId", "altId", str, False, None, False),
            ("location", "location", fhirreference.FHIRReference, False, None, False),
            ("media", "media", coding.Coding, False, None, False),
            ("name", "name", str, False, None, False),
            ("network", "network", AuditEventParticipantNetwork, False, None, False),
            ("policy", "policy", str, True, None, False),
            ("purposeOfUse", "purposeOfUse", coding.Coding, True, None, False),
            ("reference", "reference", fhirreference.FHIRReference, False, None, False),
            ("requestor", "requestor", bool, False, None, True),
            ("role", "role", codeableconcept.CodeableConcept, True, None, False),
            ("userId", "userId", identifier.Identifier, False, None, False),
        ])
        return js


class AuditEventParticipantNetwork(backboneelement.BackboneElement):
    """ Logical network location for application activity.
    
    Logical network location for application activity, if the activity has a
    network location.
    """
    
    resource_name = "AuditEventParticipantNetwork"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.address = None  #type: str
        """ Identifier for the network access point of the user device.
        Type `str`. """
        
        self.type = None  #type: str
        """ The type of network access point.
        Type `str`. """
        
        super(AuditEventParticipantNetwork, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(AuditEventParticipantNetwork, self).elementProperties()
        js.extend([
            ("address", "address", str, False, None, False),
            ("type", "type", str, False, None, False),
        ])
        return js


class AuditEventSource(backboneelement.BackboneElement):
    """ Application systems and processes.
    """
    
    resource_name = "AuditEventSource"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.identifier = None  #type: identifier.Identifier
        """ The identity of source detecting the event.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.site = None  #type: str
        """ Logical source location within the enterprise.
        Type `str`. """
        
        self.type = None  #type: coding.Coding
        """ The type of source where event originated.
        List of `Coding` items (represented as `dict` in JSON). """
        
        super(AuditEventSource, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(AuditEventSource, self).elementProperties()
        js.extend([
            ("identifier", "identifier", identifier.Identifier, False, None, True),
            ("site", "site", str, False, None, False),
            ("type", "type", coding.Coding, True, None, False),
        ])
        return js


from . import codeableconcept
from . import coding
from . import fhirdate
from . import fhirreference
from . import identifier
