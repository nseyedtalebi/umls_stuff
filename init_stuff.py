Body_Site(description='Adrenal Glands', parent=None, umls_id='C0001625').save()
Body_Site(description='Anus', parent=None, umls_id='C0003461').save()
Body_Site(description='Appendix', parent=None, umls_id='C0003617').save()
Body_Site(description='Urinary Bladder', parent=None, umls_id='C0005682').save()
Body_Site(description='Biliary tract structure', parent=None, umls_id='C0005423').save()

bones = Body_Site(description='Bone and Joints', parent=None, umls_id='C0545594')
bones.save()
Body_Site(description='Appendicular', parent=bones, umls_id='C0222646').save()
Body_Site(description='Axial', parent=bones, umls_id='C0205131').save()
Body_Site(description='Bone structure of cranium', parent=bones, umls_id='C0037303').save()
Body_Site(description='Gnathic', parent=bones, umls_id='C0022359').save()#used umls entry for 'jaw'

Body_Site(description='Bone Marrow', parent=None, umls_id='C0005953').save()

cns = Body_Site(description='Central Nervous System', parent=None, umls_id='C3714787')
cns.save()
Body_Site(description='Brain', parent=cns, umls_id='C0006104').save()
Body_Site(description='Meninges', parent=cns, umls_id='C0025285').save()
Body_Site(description='Spinal Cord', parent=cns, umls_id='C0037925').save()

Body_Site(description='Breast', parent=None, umls_id='C0006141').save()
Body_Site(description='Large Intestine (Colon)', parent=None, umls_id='C1522281').save()
Body_Site(description='Esophagus', parent=None, umls_id='C0014876').save()
Body_Site(description='Fallopian Tube', parent=None, umls_id='C0015560').save()
Body_Site(description='Gallbladder', parent=None, umls_id='C0016976').save()

head_neck = Body_Site(description='Head and Neck', parent=None, umls_id='C0460004')
head_neck.save()
Body_Site(description='Eye/Orbit', parent=head_neck, umls_id='C3846141').save()
Body_Site(description='Larynx', parent=head_neck, umls_id='C0023078').save()
Body_Site(description='Oral Cavity Including Tongue', parent=head_neck, umls_id='C0226896').save()
Body_Site(description='Parathyroid Gland', parent=head_neck, umls_id='C0030518').save()
Body_Site(description='Pharynx', parent=head_neck, umls_id='C0031354').save()
Body_Site(description='Sinonasal Region', parent=head_neck, umls_id='C1711241').save()
Body_Site(description='Skin', parent=head_neck, umls_id='C1123023').save()
Body_Site(description='Thyroid Gland', parent=head_neck, umls_id='C0040132').save()

Body_Site(description='Heart and Blood Vessels', parent=None, umls_id='C0007226').save()

Body_Site(description='Kidney', parent=None, umls_id='C0022646').save()

Body_Site(description='Liver', parent=None, umls_id='C0023884').save()

Body_Site(description='Lung', parent=None, umls_id='C0024109').save()

Body_Site(description='Lymph Node', parent=None, umls_id='C0024204').save()

mediastinum = Body_Site(description='Mediastinum', parent=None, umls_id='C0025066')
mediastinum.save()
Body_Site(description='Thymus', parent=mediastinum, umls_id='C0040113').save()
Body_Site(description='Other', parent=mediastinum, umls_id='C0220886').save()

Body_Site(description='Omentum and Mesentery', parent=None, umls_id='C0025474').save()

Body_Site(description='Ovary', parent=None, umls_id='C0029939').save()

Body_Site(description='Pancreas', parent=None, umls_id='C0030274').save()

Body_Site(description='Penis', parent=None, umls_id='C0030851').save()

Body_Site(description='Pleura', parent=None, umls_id='C0032225').save()

Body_Site(description='Rectum', parent=None, umls_id='C0034896').save()

Body_Site(description='Salivary Gland', parent=None, umls_id='C0036098').save()

Body_Site(description='Skin and Adnexal Structures', parent=None, umls_id='C0221911').save()

small_intestine = Body_Site(description='Small Intestine', parent=None, umls_id='C0545833')
small_intestine.save()
Body_Site(description='Duodenum', parent=small_intestine, umls_id='C0013303').save()
Body_Site(description='Jejunum', parent=small_intestine, umls_id='C0022378').save()
Body_Site(description='Ileum', parent=small_intestine, umls_id='C0020885').save()

soft_tissue = Body_Site(description='Soft Tissue', parent=None, umls_id='C0225317')
soft_tissue.save()
Body_Site(description='Head and neck structure', parent=soft_tissue, umls_id='C0230082').save()
Body_Site(description='Superficial', parent=soft_tissue, umls_id='C0205124').save()
Body_Site(description='Retroperitoneum', parent=soft_tissue, umls_id='C0035359').save()

Body_Site(description='Spleen', parent=None, umls_id='C0037993').save()

Body_Site(description='Stomach', parent=None, umls_id='C0038351').save()

Body_Site(description='Testis', parent=None, umls_id='C0039597').save()

Body_Site(description='Prostate', parent=None, umls_id='C0033572').save()

Body_Site(description='Ureter', parent=None, umls_id='C0041951').save()

uterus = Body_Site(description='Uterus', parent=None, umls_id='C0042149')
uterus.save()
Body_Site(description='Uterine Cervix', parent=uterus, umls_id='C0007874').save()
Body_Site(description='Endometrium', parent=uterus, umls_id='C0014180').save()
Body_Site(description='Myometrium', parent=uterus, umls_id='C0027088').save()

Body_Site(description='Vagina', parent=None, umls_id='C0042232').save()

Body_Site(description='Vulva', parent=None, umls_id='C0042993').save()