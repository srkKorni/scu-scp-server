import requests
import urllib3
import logging
requests.urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning)

def upload_dicom_file_to_orthanc_server(file_path, orthanc_url):
    """
    Uploads a DICOM file to an Orthanc server.

    Args:
    - file_path (str): Path to the DICOM file.
    - orthanc_url (str): URL of the Orthanc server endpoint for uploading instances.

    Returns:
    - bool: True if the upload is successful, False otherwise.
    """

    try:
        # Open the DICOM file and read its content
        with open(file_path, 'rb') as f:
            dicom_content = f.read()
        headers = {
            'Authorization': f'Basic T3J0aGFuYzpPcnRoYW5jQDEyMzQ='
        }
        # Send the DICOM file to the Orthanc server using POST request
        response = requests.post(orthanc_url,headers=headers, data=dicom_content, verify=False)
        print(response)
        # Check if the request was successful
        if response.status_code == 200:
            print("DICOM file uploaded successfully to Orthanc server.")
            print(response.content)
            print(response.json())
            study_id = response.json()['ID']
            print("Study ID:", study_id)
            patient_id = response.json()['ParentPatient']
            print("parent patient:",patient_id)
            return True
        else:
            print("Error uploading DICOM file:", response.text)
            return False

    except Exception as e:
        print("An error occurred:", e)
        return False

# Example usage:

# orthanc_url = 'https://pacs.smaro.app/orthanc/instances'

# if upload_dicom_file_to_orthanc_server(file_path, orthanc_url):
#     print("DICOM file uploaded successfully.")
# else:
#     print("Failed to upload DICOM file.")
