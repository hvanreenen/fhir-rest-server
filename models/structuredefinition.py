#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/StructureDefinition) on 2016-10-07.
#  2016, SMART Health IT.


from . import domainresource

class StructureDefinition(domainresource.DomainResource):
    """ Structural Definition.
    
    A definition of a FHIR structure. This resource is used to describe the
    underlying resources, data types defined in FHIR, and also for describing
    extensions, and constraints on resources and data types.
    """
    
    resource_name = "StructureDefinition"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.abstract = None  #type: bool
        """ Whether the structure is abstract.
        Type `bool`. """
        
        self.base = None  #type: str
        """ Structure that this set of constraints applies to.
        Type `str`. """
        
        self.code = None  #type: coding.Coding
        """ Assist with indexing and finding.
        List of `Coding` items (represented as `dict` in JSON). """
        
        self.constrainedType = None  #type: str
        """ Any datatype or resource, including abstract ones.
        Type `str`. """
        
        self.contact = None  #type: StructureDefinitionContact
        """ Contact details of the publisher.
        List of `StructureDefinitionContact` items (represented as `dict` in JSON). """
        
        self.context = None  #type: str
        """ Where the extension can be used in instances.
        List of `str` items. """
        
        self.contextType = None  #type: str
        """ resource | datatype | mapping | extension.
        Type `str`. """
        
        self.copyright = None  #type: str
        """ Use and/or publishing restrictions.
        Type `str`. """
        
        self.date = None  #type: fhirdate.FHIRDate
        """ Date for this version of the StructureDefinition.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None  #type: str
        """ Natural language description of the StructureDefinition.
        Type `str`. """
        
        self.differential = None  #type: StructureDefinitionDifferential
        """ Differential view of the structure.
        Type `StructureDefinitionDifferential` (represented as `dict` in JSON). """
        
        self.display = None  #type: str
        """ Use this name when displaying the value.
        Type `str`. """
        
        self.experimental = None  #type: bool
        """ If for testing purposes, not real usage.
        Type `bool`. """
        
        self.fhirVersion = None  #type: str
        """ FHIR Version this StructureDefinition targets.
        Type `str`. """
        
        self.identifier = None  #type: identifier.Identifier
        """ Other identifiers for the StructureDefinition.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.kind = None  #type: str
        """ datatype | resource | logical.
        Type `str`. """
        
        self.mapping = None  #type: StructureDefinitionMapping
        """ External specification that the content is mapped to.
        List of `StructureDefinitionMapping` items (represented as `dict` in JSON). """
        
        self.name = None  #type: str
        """ Informal name for this StructureDefinition.
        Type `str`. """
        
        self.publisher = None  #type: str
        """ Name of the publisher (Organization or individual).
        Type `str`. """
        
        self.requirements = None  #type: str
        """ Scope and Usage this structure definition is for.
        Type `str`. """
        
        self.snapshot = None  #type: StructureDefinitionSnapshot
        """ Snapshot view of the structure.
        Type `StructureDefinitionSnapshot` (represented as `dict` in JSON). """
        
        self.status = None  #type: str
        """ draft | active | retired.
        Type `str`. """
        
        self.url = None  #type: str
        """ Absolute URL used to reference this StructureDefinition.
        Type `str`. """
        
        self.useContext = None  #type: codeableconcept.CodeableConcept
        """ Content intends to support these contexts.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.version = None  #type: str
        """ Logical id for this version of the StructureDefinition.
        Type `str`. """
        
        super(StructureDefinition, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(StructureDefinition, self).elementProperties()
        js.extend([
            ("abstract", "abstract", bool, False, None, True),
            ("base", "base", str, False, None, False),
            ("code", "code", coding.Coding, True, None, False),
            ("constrainedType", "constrainedType", str, False, None, False),
            ("contact", "contact", StructureDefinitionContact, True, None, False),
            ("context", "context", str, True, None, False),
            ("contextType", "contextType", str, False, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("differential", "differential", StructureDefinitionDifferential, False, None, False),
            ("display", "display", str, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("fhirVersion", "fhirVersion", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("kind", "kind", str, False, None, True),
            ("mapping", "mapping", StructureDefinitionMapping, True, None, False),
            ("name", "name", str, False, None, True),
            ("publisher", "publisher", str, False, None, False),
            ("requirements", "requirements", str, False, None, False),
            ("snapshot", "snapshot", StructureDefinitionSnapshot, False, None, False),
            ("status", "status", str, False, None, True),
            ("url", "url", str, False, None, True),
            ("useContext", "useContext", codeableconcept.CodeableConcept, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class StructureDefinitionContact(backboneelement.BackboneElement):
    """ Contact details of the publisher.
    
    Contacts to assist a user in finding and communicating with the publisher.
    """
    
    resource_name = "StructureDefinitionContact"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None  #type: str
        """ Name of a individual to contact.
        Type `str`. """
        
        self.telecom = None  #type: contactpoint.ContactPoint
        """ Contact details for individual or publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(StructureDefinitionContact, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(StructureDefinitionContact, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


class StructureDefinitionDifferential(backboneelement.BackboneElement):
    """ Differential view of the structure.
    
    A differential view is expressed relative to the base StructureDefinition -
    a statement of differences that it applies.
    """
    
    resource_name = "StructureDefinitionDifferential"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.element = None  #type: elementdefinition.ElementDefinition
        """ Definition of elements in the resource (if no StructureDefinition).
        List of `ElementDefinition` items (represented as `dict` in JSON). """
        
        super(StructureDefinitionDifferential, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(StructureDefinitionDifferential, self).elementProperties()
        js.extend([
            ("element", "element", elementdefinition.ElementDefinition, True, None, True),
        ])
        return js


class StructureDefinitionMapping(backboneelement.BackboneElement):
    """ External specification that the content is mapped to.
    
    An external specification that the content is mapped to.
    """
    
    resource_name = "StructureDefinitionMapping"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.comments = None  #type: str
        """ Versions, Issues, Scope limitations etc..
        Type `str`. """
        
        self.identity = None  #type: str
        """ Internal id when this mapping is used.
        Type `str`. """
        
        self.name = None  #type: str
        """ Names what this mapping refers to.
        Type `str`. """
        
        self.uri = None  #type: str
        """ Identifies what this mapping refers to.
        Type `str`. """
        
        super(StructureDefinitionMapping, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(StructureDefinitionMapping, self).elementProperties()
        js.extend([
            ("comments", "comments", str, False, None, False),
            ("identity", "identity", str, False, None, True),
            ("name", "name", str, False, None, False),
            ("uri", "uri", str, False, None, False),
        ])
        return js


class StructureDefinitionSnapshot(backboneelement.BackboneElement):
    """ Snapshot view of the structure.
    
    A snapshot view is expressed in a stand alone form that can be used and
    interpreted without considering the base StructureDefinition.
    """
    
    resource_name = "StructureDefinitionSnapshot"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.element = None  #type: elementdefinition.ElementDefinition
        """ Definition of elements in the resource (if no StructureDefinition).
        List of `ElementDefinition` items (represented as `dict` in JSON). """
        
        super(StructureDefinitionSnapshot, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(StructureDefinitionSnapshot, self).elementProperties()
        js.extend([
            ("element", "element", elementdefinition.ElementDefinition, True, None, True),
        ])
        return js


from . import codeableconcept
from . import coding
from . import contactpoint
from . import elementdefinition
from . import fhirdate
from . import identifier
