import My_Function, cv2, glob, pywt

segment = My_Function.allFunction
spectrum = My_Function.allFunction
entropy = list()
energy = list()

for img in glob.glob('D:/CIKABAYAN/00Test Data/*.jpg'):
    img_GR = segment.imInput1(img) # Channel Green - Red
    img_RG = segment.imInput2(img) # Channel Red - Green
    coeff1 = pywt.dwt2(img_GR, "db2")
    LLgr, (LHgr, HLgr, HHgr) = coeff1
    # coeff2 = pywt.dwt2(img_RG, "db2")
    # LLrg, (LHrg, HLrg, HHrg) = coeff2

    #--- Print Hasil Ploting Wavelet
    cv2.imwrite(img + 'Hasil_Area_Cikabayan_GR-lv1-(A).png', LLgr)
    # cv2.imwrite(img + 'Hasil_Area_Cikabayan_RG-lv1-(A).png', LLrg)
    # cv2.imwrite(img + 'Hasil_Area_Cikabayan_GR-lv1-(V).png', LH)
    # cv2.imwrite(img + 'Hasil_Area_Cikabayan_GR-lv1-(H).png', HL)
    # cv2.imwrite(img + 'Hasil_Area_Cikabayan_GR-lv1-(D).png', HH)

    # spectrum.spectrum_print(LLgr, img + 'Hasil-Area_Cikabayan-(a)_GR-lv1')
    # spectrum.spectrum_print(LLrg, img + 'Hasil-Area_Cikabayan-(a)_RG-lv1')
