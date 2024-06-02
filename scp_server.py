from pynetdicom import AE, evt, AllStoragePresentationContexts, debug_logger
from scu_client import send_dicom
from send_dcm import upload_dicom_file_to_orthanc_server
debug_logger()
print("Initializing DICOM SCP server...")

def handle_store(event):
    """Handle a C-STORE request event."""
    ds = event.dataset
    ds.file_meta = event.file_meta
    ds.save_as(f"output_dcm/{ds.SOPInstanceUID}.dcm", write_like_original=False)
    #send_dicom(f'output_dcm/{ds.SOPInstanceUID}.dcm', '13.235.132.228', 4242, ae_title="ORTHANC")
    # initiate a scu client 
    file_path = f'output_dcm/{ds.SOPInstanceUID}.dcm'
    orthanc_url = 'https://pacs.smaro.app/orthanc/instances'
    if upload_dicom_file_to_orthanc_server(file_path, orthanc_url):
        print("DICOM file uploaded successfully.")
    else:
        print("Failed to upload DICOM file.")

    return 0x0000

handlers = [(evt.EVT_C_STORE, handle_store)]

ae = AE(ae_title='dummy')
ae.supported_contexts = AllStoragePresentationContexts

print("Starting server...")
ae.start_server(('0.0.0.0', 11112), evt_handlers=handlers)
print("Server started.")