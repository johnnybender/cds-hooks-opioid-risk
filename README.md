# Description

This project was created during the [US/UK Data Analyst Exchange Program](https://www.hhs.gov/idealab/2018/03/15/data-analyst-exchange-program-aims-to-share-data-management-and-analysis-lessons-learned-from-across-the-globe/). It is a [CDSHooks](https://cds-hooks.org/) server that can push recommendations to a CDSHooks compliant application using the CDSHook [`medication-prescribe`](https://cds-hooks.org/hooks/medication-prescribe/). This was used to demonstrate how the results of a opioid risk stratification tool could be presented to providers at the point of care. Providers could use the information from the opioid risk stratification tool to identify patients at high-risk of opioid addiction, which could prompt providers to recommend addiction prevention / support programs.

# Usage

Fork / download this repository. Documentation for the project is in the "documentation" folder. The application is the "app.py" file in the "PY3" folder. Virtual environment, and functionality to only display CDSHooks card based on type of medication prescribed have not been added. Start the Flask server and add the CDS Service to demo here: [CDSHooks Sandbox](https://sandbox.cds-hooks.org/) For any questions, please feel free to email: johnphillipbender@gmail.com.
