-- todo use table-design of http://fhirbase.github.io/
CREATE TABLE res
(
  id serial NOT NULL,
  type text,
  json text,
  CONSTRAINT pk PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE res
  OWNER TO postgres;