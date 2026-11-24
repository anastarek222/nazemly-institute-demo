# Nazemly — Institute Demo

Educational employee management demonstration using sample data only.

This repository contains the **approved cloud demo source archive** and a minimal Dockerfile. During deployment Docker extracts `source.zip`, then starts `cloud_launch.py`.

## Hosting
Render Free (Python + SQLite). SQLite data is ephemeral on the free service; any changes made during the demo might be lost when the service restarts or sleeps.

Set both secret environment variables on Render:
- `NAZEMLY_ADMIN_PASSWORD`
- `NAZEMLY_EMPLOYEE_PASSWORD`

Do not put real company information into the demonstration or use this deployment as a production HR system.
