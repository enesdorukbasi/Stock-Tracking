--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1
-- Dumped by pg_dump version 14.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: tblcategory; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tblcategory (
    id integer NOT NULL,
    name character varying(50)
);


ALTER TABLE public.tblcategory OWNER TO postgres;

--
-- Name: tblcategory_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.tblcategory ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.tblcategory_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: tblproduct; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tblproduct (
    id integer NOT NULL,
    name character varying(50),
    number integer,
    price double precision,
    categoryid integer
);


ALTER TABLE public.tblproduct OWNER TO postgres;

--
-- Name: tblproduct_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.tblproduct ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.tblproduct_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: tblsales; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tblsales (
    id integer NOT NULL,
    productid integer,
    number integer,
    price double precision
);


ALTER TABLE public.tblsales OWNER TO postgres;

--
-- Name: tblsales_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.tblsales ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.tblsales_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Data for Name: tblcategory; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tblcategory (id, name) FROM stdin;
\.


--
-- Data for Name: tblproduct; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tblproduct (id, name, number, price, categoryid) FROM stdin;
\.


--
-- Data for Name: tblsales; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tblsales (id, productid, number, price) FROM stdin;
\.


--
-- Name: tblcategory_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tblcategory_id_seq', 1, true);


--
-- Name: tblproduct_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tblproduct_id_seq', 1, true);


--
-- Name: tblsales_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tblsales_id_seq', 1, false);


--
-- Name: tblcategory tblcategory_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tblcategory
    ADD CONSTRAINT tblcategory_pkey PRIMARY KEY (id);


--
-- Name: tblproduct tblproduct_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tblproduct
    ADD CONSTRAINT tblproduct_pkey PRIMARY KEY (id);


--
-- Name: tblsales tblsales_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tblsales
    ADD CONSTRAINT tblsales_pkey PRIMARY KEY (id);


--
-- Name: tblproduct fk_category; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tblproduct
    ADD CONSTRAINT fk_category FOREIGN KEY (categoryid) REFERENCES public.tblcategory(id) ON DELETE CASCADE;


--
-- Name: tblsales fk_productid; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tblsales
    ADD CONSTRAINT fk_productid FOREIGN KEY (productid) REFERENCES public.tblproduct(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

