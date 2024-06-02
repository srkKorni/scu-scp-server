from scu_client import send_dicom

# Send the sample DICOM file to the SCP
send_dicom('dicom_files/IM-0001-0074.dcmfe2f32c2-0564-45a2-9aa7-6c71c6a6913d.dcm', '127.0.0.1', 11112, "dummy")
# send_dicom('dicom_files/sample_data.dcm', '13.235.132.228', 4242)
