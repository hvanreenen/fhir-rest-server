#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/CommunicationRequest) on 2016-10-07.
#  2016, SMART Health IT.


from . import domainresource

class CommunicationRequest(domainresource.DomainResource):
    """ A request for information to be sent to a receiver.
    
    A request to convey information; e.g. the CDS system proposes that an alert
    be sent to a responsible provider, the CDS system proposes that the public
    health agency be notified about a reportable condition.
    """
    
    resource_name = "CommunicationRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None  #type: codeableconcept.CodeableConcept
        """ Message category.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.encounter = None  #type: fhirreference.FHIRReference
        """ Encounter leading to message.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.identifier = None  #type: identifier.Identifier
        """ Unique identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.medium = None  #type: codeableconcept.CodeableConcept
        """ A channel of communication.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.payload = None  #type: CommunicationRequestPayload
        """ Message payload.
        List of `CommunicationRequestPayload` items (represented as `dict` in JSON). """
        
        self.priority = None  #type: codeableconcept.CodeableConcept
        """ Message urgency.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reason = None  #type: codeableconcept.CodeableConcept
        """ Indication for message.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.recipient = None  #type: fhirreference.FHIRReference
        """ Message recipient.
        List of `FHIRReference` items referencing `Device, Organization, Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON). """
        
        self.requestedOn = None  #type: fhirdate.FHIRDate
        """ When ordered or proposed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.requester = None  #type: fhirreference.FHIRReference
        """ An individual who requested a communication.
        Type `FHIRReference` referencing `Practitioner, Patient, RelatedPerson` (represented as `dict` in JSON). """
        
        self.scheduledDateTime = None  #type: fhirdate.FHIRDate
        """ When scheduled.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.scheduledPeriod = None  #type: period.Period
        """ When scheduled.
        Type `Period` (represented as `dict` in JSON). """
        
        self.sender = None  #type: fhirreference.FHIRReference
        """ Message sender.
        Type `FHIRReference` referencing `Device, Organization, Patient, Practitioner, RelatedPerson` (represented as `dict` in JSON). """
        
        self.status = None  #type: str
        """ proposed | planned | requested | received | accepted | in-progress
        | completed | suspended | rejected | failed.
        Type `str`. """
        
        self.subject = None  #type: fhirreference.FHIRReference
        """ Focus of message.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        super(CommunicationRequest, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(CommunicationRequest, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, False, None, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("medium", "medium", codeableconcept.CodeableConcept, True, None, False),
            ("payload", "payload", CommunicationRequestPayload, True, None, False),
            ("priority", "priority", codeableconcept.CodeableConcept, False, None, False),
            ("reason", "reason", codeableconcept.CodeableConcept, True, None, False),
            ("recipient", "recipient", fhirreference.FHIRReference, True, None, False),
            ("requestedOn", "requestedOn", fhirdate.FHIRDate, False, None, False),
            ("requester", "requester", fhirreference.FHIRReference, False, None, False),
            ("scheduledDateTime", "scheduledDateTime", fhirdate.FHIRDate, False, "scheduled", False),
            ("scheduledPeriod", "scheduledPeriod", period.Period, False, "scheduled", False),
            ("sender", "sender", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, False),
            ("subject", "subject", fhirreference.FHIRReference, False, None, False),
        ])
        return js


from . import backboneelement

class CommunicationRequestPayload(backboneelement.BackboneElement):
    """ Message payload.
    
    Text, attachment(s), or resource(s) to be communicated to the recipient.
    """
    
    resource_name = "CommunicationRequestPayload"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contentAttachment = None  #type: attachment.Attachment
        """ Message part content.
        Type `Attachment` (represented as `dict` in JSON). """
        
        self.contentReference = None  #type: fhirreference.FHIRReference
        """ Message part content.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.contentString = None  #type: str
        """ Message part content.
        Type `str`. """
        
        super(CommunicationRequestPayload, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(CommunicationRequestPayload, self).elementProperties()
        js.extend([
            ("contentAttachment", "contentAttachment", attachment.Attachment, False, "content", True),
            ("contentReference", "contentReference", fhirreference.FHIRReference, False, "content", True),
            ("contentString", "contentString", str, False, "content", True),
        ])
        return js


from . import attachment
from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import period
