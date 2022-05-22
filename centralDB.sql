CREATE TABLE IF NOT EXISTS "resultsPING" (
    "fw" INT,
    "lts" INT,
    "dst_name" TEXT,
    "af" INT,
    "dst_addr" TEXT,
    "src_addr" TEXT,
    "proto" TEXT,
    "size" INT,
    "result_x" TEXT,
    "dup" INT,
    "rcvd" INT,
    "sent" INT,
    "min" INT,
    "max" INT,
    "avg" INT,
    "msm_id" INT,
    "prb_id" INT,
    "timestamp" INT,
    "msm_name" TEXT,
    "from" TEXT,
    "type" TEXT,
    "group_id" INT,
    "step" INT,
    "stored_timestamp" INT,
	PRIMARY KEY (timestamp,msm_id)
);

INSERT INTO "results" VALUES
    (4790,36,'13.34.55.160',4,'13.34.55.160','192.168.178.26','ICMP',20,'*',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
    (4790,36,'13.34.55.160',4,'13.34.55.160','192.168.178.26','ICMP',20,NULL,0,0,1,-1,-1,-1,41329425,1,1653222181,'Ping','45.138.229.91','ping',41329425,0,1653222183);