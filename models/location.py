#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Location) on 2016-10-07.
#  2016, SMART Health IT.


from . import domainresource

class Location(domainresource.DomainResource):
    """ Details and position information for a physical place.
    
    Details and position information for a physical place where services are
    provided  and resources and participants may be stored, found, contained or
    accommodated.
    """
    
    resource_name = "Location"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.address = None  #type: address.Address
        """ Physical location.
        Type `Address` (represented as `dict` in JSON). """
        
        self.description = None  #type: str
        """ Description of the location.
        Type `str`. """
        
        self.identifier = None  #type: identifier.Identifier
        """ Unique code or number identifying the location to its users.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.managingOrganization = None  #type: fhirreference.FHIRReference
        """ Organization responsible for provisioning and upkeep.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.mode = None  #type: str
        """ instance | kind.
        Type `str`. """
        
        self.name = None  #type: str
        """ Name of the location as used by humans.
        Type `str`. """
        
        self.partOf = None  #type: fhirreference.FHIRReference
        """ Another Location this one is physically part of.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.physicalType = None  #type: codeableconcept.CodeableConcept
        """ Physical form of the location.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.position = None  #type: LocationPosition
        """ The absolute geographic location.
        Type `LocationPosition` (represented as `dict` in JSON). """
        
        self.status = None  #type: str
        """ active | suspended | inactive.
        Type `str`. """
        
        self.telecom = None  #type: contactpoint.ContactPoint
        """ Contact details of the location.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        self.type = None  #type: codeableconcept.CodeableConcept
        """ Type of function performed.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Location, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(Location, self).elementProperties()
        js.extend([
            ("address", "address", address.Address, False, None, False),
            ("description", "description", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("managingOrganization", "managingOrganization", fhirreference.FHIRReference, False, None, False),
            ("mode", "mode", str, False, None, False),
            ("name", "name", str, False, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, False, None, False),
            ("physicalType", "physicalType", codeableconcept.CodeableConcept, False, None, False),
            ("position", "position", LocationPosition, False, None, False),
            ("status", "status", str, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, False, None, False),
        ])
        return js


from . import backboneelement

class LocationPosition(backboneelement.BackboneElement):
    """ The absolute geographic location.
    
    The absolute geographic location of the Location, expressed using the WGS84
    datum (This is the same co-ordinate system used in KML).
    """
    
    resource_name = "LocationPosition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.altitude = None  #type: float
        """ Altitude with WGS84 datum.
        Type `float`. """
        
        self.latitude = None  #type: float
        """ Latitude with WGS84 datum.
        Type `float`. """
        
        self.longitude = None  #type: float
        """ Longitude with WGS84 datum.
        Type `float`. """
        
        super(LocationPosition, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(LocationPosition, self).elementProperties()
        js.extend([
            ("altitude", "altitude", float, False, None, False),
            ("latitude", "latitude", float, False, None, True),
            ("longitude", "longitude", float, False, None, True),
        ])
        return js


from . import address
from . import codeableconcept
from . import contactpoint
from . import fhirreference
from . import identifier
