# MXLIMS data model

The MXLIMS data model is a collaborative data model to serve for both API specification and
potentially as the basis for data storage solutions, for macromolecular crystallography and
related scientific areas. For more detailed overview documentation see the other files in this directory. 


## JSON schemas

The JSON schemas in mxlims/schemas are the authoritative version of the data model.
They are organised as follows:

  - schemas/core contain the abstract classes that define the links and foreign keys
  that are used to represent the model in a (MongoDB-type) database.

  - schemas/datatypes contain all datatypes, i.e. schemas for data that do not have an
  object ID, compare by value, and that can be used in any context. One example is the
  definitions of enumerations.

  - schemas/rawobjects contain supported objects together with the definitions of their
  fields, those that would be represented as metadata in an ICAT-type database.
  These can be used with the GeneralMessage.json to represent any combination of objects,
  but they lack 1) the faculty for hierarchically nesting objects, 2) the constraints
  on which types of objects can be linked, the links being defined only by untyped foreign keys.

  - schemas/objects contain subtypes of the rawobjects with the hierarchical JSON
  containment and the constraints on interobject links added. These are the schemas
  one would use for messages with hierarchical objects, e.g. for normal shipping manifests
  or for any 'human-readable' messages.

  - schemas/messages contain key examples of messages for sending combinations of objects,
  which together serve as starting points for the entire model. See next section for details.


## JSON html documentation

docs/html contains linked html files for all JSON objects and datatypes in the model.

The documentation is generated using the program https://coveooss.github.io/json-schema-for-humans/#/
with the command (starting in the mxlims directory)

generate-schema-doc --config-file docs/schemadoc_config.json schemas docs/html

To cover the entire model starting from the top containers you should begin with the following files>

  - docs/html/GeneralMessage.html
  This message contains all objects in their 'raw' form as a single layer of objects
   i.e. excluding the JSON fields that define hierarchical containment.
   The GeneralMessage can be used to transfer any possible combination of objects.
   In the absence of the contained objects all interobject links must be generated
   from the uuid fields as for a database. Also the schemas in this message
   do not contain the constraints on the types of linked objects that can be linked
   that are defined in the full object schemas.

  - docs/html/ShipmentMessage.html
  This is the message that would normally be used for a shipment. It contains
  a hierarchy of contained objects and includes all links and constraints in the model
  except for those describing the contained objects of PreparedSamples. These links must
  be generated from the uuid fields in the various LogisticalSamples

  - docs/html/SamplesMessage.html
  This message covers PreparedSamples and their (recursive, hierarchical) contents,
  and includes all the links and constraints that were omitted in the ShipmentMessage.
  It does not include the 'outermost' LogisticalSample objects: Shipment, Dewar, Puck, and Plate.

## Pydantic

The pydantic files are generated from the JSON schemas using
https://docs.pydantic.dev/latest/integrations/datamodel_code_generator/
with the command (starting in the mxlims directory)

datamodel-codegen --input-file-type jsonschema --output-model-type pydantic_v2.BaseModel  --base-class mxlims.pydantic.MxBaseModel.BaseModel --use-schema-description --use-double-quotes --disable-timestamp --use-default --target-python-version 3.10 --snake-case-field --use-exact-imports --capitalise-enum-members --use-title-as-name --use-one-literal-as-default --input schemas --output pydantic

The Pydantic should be a faithful copy of the model in the JSON schemas, except that
it may lack certain constraints. For instance the constraint that a Dataset cannot
have both sourceId and derivedFromId non-null is enforced in the JSON but not in Pydantic.