#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Substance) on 2016-10-07.
#  2016, SMART Health IT.


from . import domainresource

class Substance(domainresource.DomainResource):
    """ A homogeneous material with a definite composition.
    """
    
    resource_name = "Substance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.category = None  #type: codeableconcept.CodeableConcept
        """ What class/type of substance this is.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.code = None  #type: codeableconcept.CodeableConcept
        """ What substance this is.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.description = None  #type: str
        """ Textual description of the substance, comments.
        Type `str`. """
        
        self.identifier = None  #type: identifier.Identifier
        """ Unique identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.ingredient = None  #type: SubstanceIngredient
        """ Composition information about the substance.
        List of `SubstanceIngredient` items (represented as `dict` in JSON). """
        
        self.instance = None  #type: SubstanceInstance
        """ If this describes a specific package/container of the substance.
        List of `SubstanceInstance` items (represented as `dict` in JSON). """
        
        super(Substance, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(Substance, self).elementProperties()
        js.extend([
            ("category", "category", codeableconcept.CodeableConcept, True, None, False),
            ("code", "code", codeableconcept.CodeableConcept, False, None, True),
            ("description", "description", str, False, None, False),
            ("identifier", "identifier", identifier.Identifier, True, None, False),
            ("ingredient", "ingredient", SubstanceIngredient, True, None, False),
            ("instance", "instance", SubstanceInstance, True, None, False),
        ])
        return js


from . import backboneelement

class SubstanceIngredient(backboneelement.BackboneElement):
    """ Composition information about the substance.
    
    A substance can be composed of other substances.
    """
    
    resource_name = "SubstanceIngredient"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.quantity = None  #type: ratio.Ratio
        """ Optional amount (concentration).
        Type `Ratio` (represented as `dict` in JSON). """
        
        self.substance = None  #type: fhirreference.FHIRReference
        """ A component of the substance.
        Type `FHIRReference` referencing `Substance` (represented as `dict` in JSON). """
        
        super(SubstanceIngredient, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(SubstanceIngredient, self).elementProperties()
        js.extend([
            ("quantity", "quantity", ratio.Ratio, False, None, False),
            ("substance", "substance", fhirreference.FHIRReference, False, None, True),
        ])
        return js


class SubstanceInstance(backboneelement.BackboneElement):
    """ If this describes a specific package/container of the substance.
    
    Substance may be used to describe a kind of substance, or a specific
    package/container of the substance: an instance.
    """
    
    resource_name = "SubstanceInstance"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.expiry = None  #type: fhirdate.FHIRDate
        """ When no longer valid to use.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier = None  #type: identifier.Identifier
        """ Identifier of the package/container.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.quantity = None  #type: quantity.Quantity
        """ Amount of substance in the package.
        Type `Quantity` referencing `SimpleQuantity` (represented as `dict` in JSON). """
        
        super(SubstanceInstance, self).__init__(jsondict=jsondict, strict=strict)

    def __str__(self):
        return '' 
    
    def elementProperties(self):
        js = super(SubstanceInstance, self).elementProperties()
        js.extend([
            ("expiry", "expiry", fhirdate.FHIRDate, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("quantity", "quantity", quantity.Quantity, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import quantity
from . import ratio
