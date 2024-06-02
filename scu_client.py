from pydicom import dcmread
from pynetdicom import AE, StoragePresentationContexts

def send_dicom(file_path, addr, port, ae_title):
    ae = AE()
    ae.requested_contexts = StoragePresentationContexts
    ds = dcmread(file_path)
    
    assoc = ae.associate(addr, port, ae_title=ae_title)
    if assoc.is_established:
        status = assoc.send_c_store(ds)
        if status:
            print(f'C-STORE request status: 0x{status.Status:04x}')
        else:
            print('Connection timed out, was aborted or received invalid response')
        assoc.release()
    else:
        print('Association rejected, aborted or never connected')
