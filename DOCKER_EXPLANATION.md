# Docker Setup Explanation

## Problem: ARM64 (Apple Silicon) Compatibility
 
MongoDB 4.4 doesn't have native ARM64 packages, causing build failures.

## Solution:

### Changes Made to `docker-compose.yml`

**Added `platform: linux/amd64` to all services**

This Runs containers in x86_64 mode on ARM Macs using emulation and 
All three containers (api, app, mongo) use the same architecture

### Changes Made to `Dockerfile`

#### 1. Changed Base Image
Uses Debian Buster specifically (needed for MongoDB 4.4 compatibility)

#### 2. Fixed Archived Debian Repositories

Did this because Debian Buster reached end-of-life and moved to archive repositories

#### 3. Updated MongoDB Installation
Uses modern GPG keyring method instead of deprecated `apt-key`

#### 4. Removed Deprecated `easy_install`

`easy_install` command no longer exists in modern Python

---

