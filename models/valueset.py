#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/ValueSet) on 2016-10-07.
#  2016, SMART Health IT.


from . import domainresource

class ValueSet(domainresource.DomainResource):
    """ A set of codes drawn from one or more code systems.
    
    A value set specifies a set of codes drawn from one or more code systems.
    """
    
    resource_name = "ValueSet"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.codeSystem = None  #type: ValueSetCodeSystem
        """ An inline code system, which is part of this value set.
        Type `ValueSetCodeSystem` (represented as `dict` in JSON). """
        
        self.compose = None  #type: ValueSetCompose
        """ When value set includes codes from elsewhere.
        Type `ValueSetCompose` (represented as `dict` in JSON). """
        
        self.contact = None  #type: ValueSetContact
        """ Contact details of the publisher.
        List of `ValueSetContact` items (represented as `dict` in JSON). """
        
        self.copyright = None  #type: str
        """ Use and/or publishing restrictions.
        Type `str`. """
        
        self.date = None  #type: fhirdate.FHIRDate
        """ Date for given status.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.description = None  #type: str
        """ Human language description of the value set.
        Type `str`. """
        
        self.expansion = None  #type: ValueSetExpansion
        """ Used when the value set is "expanded".
        Type `ValueSetExpansion` (represented as `dict` in JSON). """
        
        self.experimental = None  #type: bool
        """ If for testing purposes, not real usage.
        Type `bool`. """
        
        self.extensible = None  #type: bool
        """ Whether this is intended to be used with an extensible binding.
        Type `bool`. """
        
        self.identifier = None  #type: identifier.Identifier
        """ Additional identifier for the value set (e.g. HL7 v2 / CDA).
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.immutable = None  #type: bool
        """ Indicates whether or not any change to the content logical
        definition may occur.
        Type `bool`. """
        
        self.lockedDate = None  #type: fhirdate.FHIRDate
        """ Fixed date for all referenced code systems and value sets.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.name = None  #type: str
        """ Informal name for this value set.
        Type `str`. """
        
        self.publisher = None  #type: str
        """ Name of the publisher (organization or individual).
        Type `str`. """
        
        self.requirements = None  #type: str
        """ Why needed.
        Type `str`. """
        
        self.status = None  #type: str
        """ draft | active | retired.
        Type `str`. """
        
        self.url = None  #type: str
        """ Globally unique logical identifier for  value set.
        Type `str`. """
        
        self.useContext = None  #type: codeableconcept.CodeableConcept
        """ Content intends to support these contexts.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.version = None  #type: str
        """ Logical identifier for this version of the value set.
        Type `str`. """
        
        super(ValueSet, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(ValueSet, self).elementProperties()
        js.extend([
            ("codeSystem", "codeSystem", ValueSetCodeSystem, False, None, False),
            ("compose", "compose", ValueSetCompose, False, None, False),
            ("contact", "contact", ValueSetContact, True, None, False),
            ("copyright", "copyright", str, False, None, False),
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("description", "description", str, False, None, False),
            ("expansion", "expansion", ValueSetExpansion, False, None, False),
            ("experimental", "experimental", bool, False, None, False),
            ("extensible", "extensible", bool, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("immutable", "immutable", bool, False, None, False),
            ("lockedDate", "lockedDate", fhirdate.FHIRDate, False, None, False),
            ("name", "name", str, False, None, False),
            ("publisher", "publisher", str, False, None, False),
            ("requirements", "requirements", str, False, None, False),
            ("status", "status", str, False, None, True),
            ("url", "url", str, False, None, False),
            ("useContext", "useContext", codeableconcept.CodeableConcept, True, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


from . import backboneelement

class ValueSetCodeSystem(backboneelement.BackboneElement):
    """ An inline code system, which is part of this value set.
    
    A definition of a code system, inlined into the value set (as a packaging
    convenience). Note that the inline code system may be used from other value
    sets by referring to its (codeSystem.system) directly.
    """
    
    resource_name = "ValueSetCodeSystem"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.caseSensitive = None  #type: bool
        """ If code comparison is case sensitive.
        Type `bool`. """
        
        self.concept = None  #type: ValueSetCodeSystemConcept
        """ Concepts in the code system.
        List of `ValueSetCodeSystemConcept` items (represented as `dict` in JSON). """
        
        self.system = None  #type: str
        """ URI to identify the code system (e.g. in Coding.system).
        Type `str`. """
        
        self.version = None  #type: str
        """ Version (for use in Coding.version).
        Type `str`. """
        
        super(ValueSetCodeSystem, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(ValueSetCodeSystem, self).elementProperties()
        js.extend([
            ("caseSensitive", "caseSensitive", bool, False, None, False),
            ("concept", "concept", ValueSetCodeSystemConcept, True, None, True),
            ("system", "system", str, False, None, True),
            ("version", "version", str, False, None, False),
        ])
        return js


class ValueSetCodeSystemConcept(backboneelement.BackboneElement):
    """ Concepts in the code system.
    
    Concepts that are in the code system. The concept definitions are
    inherently hierarchical, but the definitions must be consulted to determine
    what the meaning of the hierarchical relationships are.
    """
    
    resource_name = "ValueSetCodeSystemConcept"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.abstract = None  #type: bool
        """ If this code is not for use as a real concept.
        Type `bool`. """
        
        self.code = None  #type: str
        """ Code that identifies concept.
        Type `str`. """
        
        self.concept = None  #type: ValueSetCodeSystemConcept
        """ Child Concepts (is-a/contains/categorizes).
        List of `ValueSetCodeSystemConcept` items (represented as `dict` in JSON). """
        
        self.definition = None  #type: str
        """ Formal definition.
        Type `str`. """
        
        self.designation = None  #type: ValueSetCodeSystemConceptDesignation
        """ Additional representations for the concept.
        List of `ValueSetCodeSystemConceptDesignation` items (represented as `dict` in JSON). """
        
        self.display = None  #type: str
        """ Text to display to the user.
        Type `str`. """
        
        super(ValueSetCodeSystemConcept, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(ValueSetCodeSystemConcept, self).elementProperties()
        js.extend([
            ("abstract", "abstract", bool, False, None, False),
            ("code", "code", str, False, None, True),
            ("concept", "concept", ValueSetCodeSystemConcept, True, None, False),
            ("definition", "definition", str, False, None, False),
            ("designation", "designation", ValueSetCodeSystemConceptDesignation, True, None, False),
            ("display", "display", str, False, None, False),
        ])
        return js


class ValueSetCodeSystemConceptDesignation(backboneelement.BackboneElement):
    """ Additional representations for the concept.
    
    Additional representations for the concept - other languages, aliases,
    specialized purposes, used for particular purposes, etc.
    """
    
    resource_name = "ValueSetCodeSystemConceptDesignation"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.language = None  #type: str
        """ Human language of the designation.
        Type `str`. """
        
        self.use = None  #type: coding.Coding
        """ Details how this designation would be used.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.value = None  #type: str
        """ The text value for this designation.
        Type `str`. """
        
        super(ValueSetCodeSystemConceptDesignation, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(ValueSetCodeSystemConceptDesignation, self).elementProperties()
        js.extend([
            ("language", "language", str, False, None, False),
            ("use", "use", coding.Coding, False, None, False),
            ("value", "value", str, False, None, True),
        ])
        return js


class ValueSetCompose(backboneelement.BackboneElement):
    """ When value set includes codes from elsewhere.
    
    A set of criteria that provide the content logical definition of the value
    set by including or excluding codes from outside this value set.
    """
    
    resource_name = "ValueSetCompose"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.exclude = None  #type: ValueSetComposeInclude
        """ Explicitly exclude codes.
        List of `ValueSetComposeInclude` items (represented as `dict` in JSON). """
        
        self.import_fhir = None  #type: str
        """ Import the contents of another value set.
        List of `str` items. """
        
        self.include = None  #type: ValueSetComposeInclude
        """ Include one or more codes from a code system.
        List of `ValueSetComposeInclude` items (represented as `dict` in JSON). """
        
        super(ValueSetCompose, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(ValueSetCompose, self).elementProperties()
        js.extend([
            ("exclude", "exclude", ValueSetComposeInclude, True, None, False),
            ("import_fhir", "import", str, True, None, False),
            ("include", "include", ValueSetComposeInclude, True, None, False),
        ])
        return js


class ValueSetComposeInclude(backboneelement.BackboneElement):
    """ Include one or more codes from a code system.
    """
    
    resource_name = "ValueSetComposeInclude"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.concept = None  #type: ValueSetComposeIncludeConcept
        """ A concept defined in the system.
        List of `ValueSetComposeIncludeConcept` items (represented as `dict` in JSON). """
        
        self.filter = None  #type: ValueSetComposeIncludeFilter
        """ Select codes/concepts by their properties (including relationships).
        List of `ValueSetComposeIncludeFilter` items (represented as `dict` in JSON). """
        
        self.system = None  #type: str
        """ The system the codes come from.
        Type `str`. """
        
        self.version = None  #type: str
        """ Specific version of the code system referred to.
        Type `str`. """
        
        super(ValueSetComposeInclude, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(ValueSetComposeInclude, self).elementProperties()
        js.extend([
            ("concept", "concept", ValueSetComposeIncludeConcept, True, None, False),
            ("filter", "filter", ValueSetComposeIncludeFilter, True, None, False),
            ("system", "system", str, False, None, True),
            ("version", "version", str, False, None, False),
        ])
        return js


class ValueSetComposeIncludeConcept(backboneelement.BackboneElement):
    """ A concept defined in the system.
    
    Specifies a concept to be included or excluded.
    """
    
    resource_name = "ValueSetComposeIncludeConcept"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None  #type: str
        """ Code or expression from system.
        Type `str`. """
        
        self.designation = None  #type: ValueSetCodeSystemConceptDesignation
        """ Additional representations for this valueset.
        List of `ValueSetCodeSystemConceptDesignation` items (represented as `dict` in JSON). """
        
        self.display = None  #type: str
        """ Test to display for this code for this value set.
        Type `str`. """
        
        super(ValueSetComposeIncludeConcept, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(ValueSetComposeIncludeConcept, self).elementProperties()
        js.extend([
            ("code", "code", str, False, None, True),
            ("designation", "designation", ValueSetCodeSystemConceptDesignation, True, None, False),
            ("display", "display", str, False, None, False),
        ])
        return js


class ValueSetComposeIncludeFilter(backboneelement.BackboneElement):
    """ Select codes/concepts by their properties (including relationships).
    
    Select concepts by specify a matching criteria based on the properties
    (including relationships) defined by the system. If multiple filters are
    specified, they SHALL all be true.
    """
    
    resource_name = "ValueSetComposeIncludeFilter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.op = None  #type: str
        """ = | is-a | is-not-a | regex | in | not-in.
        Type `str`. """
        
        self.property = None  #type: str
        """ A property defined by the code system.
        Type `str`. """
        
        self.value = None  #type: str
        """ Code from the system, or regex criteria.
        Type `str`. """
        
        super(ValueSetComposeIncludeFilter, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(ValueSetComposeIncludeFilter, self).elementProperties()
        js.extend([
            ("op", "op", str, False, None, True),
            ("property", "property", str, False, None, True),
            ("value", "value", str, False, None, True),
        ])
        return js


class ValueSetContact(backboneelement.BackboneElement):
    """ Contact details of the publisher.
    
    Contacts to assist a user in finding and communicating with the publisher.
    """
    
    resource_name = "ValueSetContact"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None  #type: str
        """ Name of an individual to contact.
        Type `str`. """
        
        self.telecom = None  #type: contactpoint.ContactPoint
        """ Contact details for individual or publisher.
        List of `ContactPoint` items (represented as `dict` in JSON). """
        
        super(ValueSetContact, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(ValueSetContact, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, False),
            ("telecom", "telecom", contactpoint.ContactPoint, True, None, False),
        ])
        return js


class ValueSetExpansion(backboneelement.BackboneElement):
    """ Used when the value set is "expanded".
    
    A value set can also be "expanded", where the value set is turned into a
    simple collection of enumerated codes. This element holds the expansion, if
    it has been performed.
    """
    
    resource_name = "ValueSetExpansion"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.contains = None  #type: ValueSetExpansionContains
        """ Codes in the value set.
        List of `ValueSetExpansionContains` items (represented as `dict` in JSON). """
        
        self.identifier = None  #type: str
        """ Uniquely identifies this expansion.
        Type `str`. """
        
        self.offset = None  #type: int
        """ Offset at which this resource starts.
        Type `int`. """
        
        self.parameter = None  #type: ValueSetExpansionParameter
        """ Parameter that controlled the expansion process.
        List of `ValueSetExpansionParameter` items (represented as `dict` in JSON). """
        
        self.timestamp = None  #type: fhirdate.FHIRDate
        """ Time ValueSet expansion happened.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.total = None  #type: int
        """ Total number of codes in the expansion.
        Type `int`. """
        
        super(ValueSetExpansion, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(ValueSetExpansion, self).elementProperties()
        js.extend([
            ("contains", "contains", ValueSetExpansionContains, True, None, False),
            ("identifier", "identifier", str, False, None, True),
            ("offset", "offset", int, False, None, False),
            ("parameter", "parameter", ValueSetExpansionParameter, True, None, False),
            ("timestamp", "timestamp", fhirdate.FHIRDate, False, None, True),
            ("total", "total", int, False, None, False),
        ])
        return js


class ValueSetExpansionContains(backboneelement.BackboneElement):
    """ Codes in the value set.
    
    The codes that are contained in the value set expansion.
    """
    
    resource_name = "ValueSetExpansionContains"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.abstract = None  #type: bool
        """ If user cannot select this entry.
        Type `bool`. """
        
        self.code = None  #type: str
        """ Code - if blank, this is not a selectable code.
        Type `str`. """
        
        self.contains = None  #type: ValueSetExpansionContains
        """ Codes contained under this entry.
        List of `ValueSetExpansionContains` items (represented as `dict` in JSON). """
        
        self.display = None  #type: str
        """ User display for the concept.
        Type `str`. """
        
        self.system = None  #type: str
        """ System value for the code.
        Type `str`. """
        
        self.version = None  #type: str
        """ Version in which this code/display is defined.
        Type `str`. """
        
        super(ValueSetExpansionContains, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(ValueSetExpansionContains, self).elementProperties()
        js.extend([
            ("abstract", "abstract", bool, False, None, False),
            ("code", "code", str, False, None, False),
            ("contains", "contains", ValueSetExpansionContains, True, None, False),
            ("display", "display", str, False, None, False),
            ("system", "system", str, False, None, False),
            ("version", "version", str, False, None, False),
        ])
        return js


class ValueSetExpansionParameter(backboneelement.BackboneElement):
    """ Parameter that controlled the expansion process.
    
    A parameter that controlled the expansion process. These parameters may be
    used by users of expanded value sets to check whether the expansion is
    suitable for a particular purpose, or to pick the correct expansion.
    """
    
    resource_name = "ValueSetExpansionParameter"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.name = None  #type: str
        """ Name as assigned by the server.
        Type `str`. """
        
        self.valueBoolean = None  #type: bool
        """ Value of the named parameter.
        Type `bool`. """
        
        self.valueCode = None  #type: str
        """ Value of the named parameter.
        Type `str`. """
        
        self.valueDecimal = None  #type: float
        """ Value of the named parameter.
        Type `float`. """
        
        self.valueInteger = None  #type: int
        """ Value of the named parameter.
        Type `int`. """
        
        self.valueString = None  #type: str
        """ Value of the named parameter.
        Type `str`. """
        
        self.valueUri = None  #type: str
        """ Value of the named parameter.
        Type `str`. """
        
        super(ValueSetExpansionParameter, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(ValueSetExpansionParameter, self).elementProperties()
        js.extend([
            ("name", "name", str, False, None, True),
            ("valueBoolean", "valueBoolean", bool, False, "value", False),
            ("valueCode", "valueCode", str, False, "value", False),
            ("valueDecimal", "valueDecimal", float, False, "value", False),
            ("valueInteger", "valueInteger", int, False, "value", False),
            ("valueString", "valueString", str, False, "value", False),
            ("valueUri", "valueUri", str, False, "value", False),
        ])
        return js


from . import codeableconcept
from . import coding
from . import contactpoint
from . import fhirdate
from . import identifier
