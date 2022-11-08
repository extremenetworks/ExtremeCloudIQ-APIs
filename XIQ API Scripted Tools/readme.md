# XIQ Scripted Tools
These are fully functional tools that have been developed leveraging XIQ APIs. These scripts can be used for learning or for customer use. 

If you are just getting started with these Scripts check out our Getting Started repo. This include a PDF document that walks through the basics of using these scripts.
> Link to GitHub Repo: [API_Getting_Started (v3)](https://github.com/ExtremeNetworksSA/API_Getting_Started)

-------------------
------------------
#### Table of contents
[XIQ_Ekahau_Importer](#XIQ_Ekahau_Importer)

[XIQ_WiNG_Location_Migration](#XIQ_WiNG_Location_Migration)

[XIQ_AD_PPSK_Sync](#XIQ_AD_PPSK_Sync)

[XIQ_Azure_AD_PPSK_Sync](#XIQ_Azure_AD_PPSK_Sync)

[XIQ_Gsuite_PPSK_Sync](#XIQ_Gsuite_PPSK_Sync)

[XIQ_Sync_Between_VIQs](#XIQ_Sync_Between_VIQs)

>**Note**: It is recommended to test these in pre-production to make sure you are familiar with how they work before using them on production networks.
-------------------
-------------------

## Location and Device onboarding scripts

### XIQ_Ekahau_Importer

> Link to GitHub Repo: [XIQ_Ekahau_Importer (v1.0.2)](https://github.com/ExtremeNetworksSA/XIQ_Ekahau_Importer)

This script can be used to import a Ekahau floorplan and place APs into ExtremeCloud IQ (XIQ). This will save time by creating the building and floor(s) (as well as optional location), uploading the image file, scaling the floorplan, and setting the location of the Access Points all from data within an Ekahau file. 

###### information

- There is a document file included in the GitHub repo that covers setting up the script and running it.
- Tested on MacOS only

-------------------

### XIQ_WiNG_Location_Migration

> Link to GitHub Repo: [XIQ_Wing_location_migration (v1.1.1)](https://github.com/ExtremeNetworksSA/XIQ_Wing_location_migration)

This script can be used to migrate the location hierarchy, rf-domains, and floors from WiNG to XIQ. This script will also assign APs that are configured in WiNG to the correct locations in XIQ after the locations are created. A tech-dump from the wing controller will be needed for the script. The script will parse the rf-domain data and device data using a couple files from within the tech-dump. Nothing needs to be done with the tech-dump. The script will ask for the file, just put the name of the tar.gz file (with its path).

###### information

- There is a document file included in the GitHub repo that covers setting up the script and running it.
- Tested on MacOS only

-------------------

### XIQ_Replace_AP

> Link to GitHub Repo: [XIQ_Replace_AP](https://github.com/ExtremeNetworksSA/XIQ_Examples/tree/master/v2_API_examples/Replace_AP)

This script will collect a device's hostname, location info, and network policy, onboard a new device, apply those setting to the new devices and then remove the old device from XIQ.
>**Note**: This script will **not** pull any device template overrides that could be on the existing device.

###### information

- There is a readme file included in the GitHub folder that covers running the script.
- Testing on MacOS
-------------------
-------------------
## PPSK scripts

### XIQ_AD_PPSK_Sync

> Link to GitHub Repo: [XIQ-AD-PPSK-Sync (v2.0.6.1)](https://github.com/ExtremeNetworksSA/XIQ-AD-User-Sync)

This script can be used to sync your existing local domain Active directory security group with a Private Pre-shared-key (PPSK) user group. This script will leverage your existing Active Directory security groups to automatically create a Private Pre-shared key for every AD user and remove the PPSK user if a user is disabled or removed from the group in the AD server.

###### information

- There is a document file included in the GitHub repo that covers setting up the script and running it.
- Tested on MacOS, Windows, and linux

-------------------

### XIQ_Azure_AD_PPSK_Sync

> Link to GitHub Repo: [XIQ-Azure-AD-PPSK-Sync (v1.0.0)](https://github.com/ExtremeNetworksSA/XIQ_Azure_AD_Sync)

This script can be used to sync your existing Azure (cloud-based) Active directory user group with a Private Pre-shared-key (PPSK) user group. This script will leverage your existing Azure Active Directory groups to automatically create a Private Pre-shared key for every AD user and remove the PPSK user if a user is disabled or removed from the group in Azure AD.

###### information

- There is a document file included in the GitHub repo that covers setting up the script and running it.
- Tested on MacOS, Windows, and linux

-------------------

### XIQ_Gsuite_PPSK_Sync

> Link to GitHub Repo: [XIQ-Gsuite-PPSK-Sync (v1.0.0)](https://github.com/ExtremeNetworksSA/XIQ_Gsuite_PPSK_Sync)

This script can be used to sync your existing GSuite user group with a Private Pre-shared-key (PPSK) user group. This script will leverage your existing GSuite user groups to automatically create a Private Pre-shared key for every GSuite user and remove the PPSK user if a user is disabled or removed from the group in GSuite.

###### information

- There is a document file included in the GitHub repo that covers setting up the script and running it.
- Tested on MacOS, Windows, and linux

-------------------

### XIQ_Sync_Between_VIQs

> Link to GitHub Repo: [PPSK_Sync_Between_VIQs (v2.0.0)](https://github.com/ExtremeNetworksSA/XIQ_PPSK_Sync_Between_VIQs)

This script will collect the PPSK Users from a the main VIQ account and create those same PPSK Users in all Externally Managed VIQs. The name of the user group needs to be the same on all managed accounts, including the viq they export from. If you have a specific Managed VIQ(s) you want to skip you can add the Name of the VIQ to the script to be excluded.

###### information

- There is a readme file included in the GitHub repo that covers setting up the script and running it.
- Tested on MacOS

-------------------
-------------------

## Device Management scripts

### XIQ_Staggered_Reboot

> Link to GitHub Repo [XIQ_Staggered_Reboot (v1.0.0)](https://github.com/ExtremeNetworksSA/XIQ_Staggered_Reboot)

This script will reboot devices 1 at a time, wait up to 15 mins for the device to come back online. Once the device is back online the script will proceed to reboot the next device. You can do all devices within your XIQ instance or filter to a specific building. If the device does not come back online within the 15 mins the script will pause and ask if it should continue or not.

###### information

- There is a readme file included in the GitHub repo that covers setting up the script and running it.
- Tested on MacOS

-------------------