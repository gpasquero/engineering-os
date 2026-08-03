# Architecture

Two modules. `billing` owns invoices and refunds; `accounts` owns tenants and
their users. Every account row carries `tenant_id` and every query is expected
to filter on it.
