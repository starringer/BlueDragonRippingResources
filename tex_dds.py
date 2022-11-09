from inc_noesis import *

def registerNoesisTypes():
    handle = noesis.register("Some unknown X360 texture", ".dds")
    noesis.setHandlerTypeCheck(handle, noepyCheckType)
    noesis.setHandlerLoadRGBA(handle, noepyLoadRGBA)
    #noesis.logPopup()
    return 1

def noepyCheckType(data):
    return 1

def noepyLoadRGBA(data, texList):
    bs = NoeBitStream(data)
    dataOffset = 0x800       #set the data offset
    datasize = bs.getSize() - dataOffset
    imgFmt = 3               #set image format (1 - 7)
    imgWidth = 1024          #set image width
    imgHeight = 1024          #set image height
    bs.seek(dataOffset, NOESEEK_ABS)
    data = bs.readBytes(datasize)
    #DXT1
    if imgFmt == 1:
        data = rapi.imageUntile360DXT(rapi.swapEndianArray(data, 2), imgWidth, imgHeight, 8)
        texFmt = noesis.NOESISTEX_DXT1
    #DXT3
    elif imgFmt == 2:
        data = rapi.imageUntile360DXT(rapi.swapEndianArray(data, 2), imgWidth, imgHeight, 16)
        texFmt = noesis.NOESISTEX_DXT3
    #DXT5
    elif imgFmt == 3:
        data = rapi.imageUntile360DXT(rapi.swapEndianArray(data, 2), imgWidth, imgHeight, 16)
        texFmt = noesis.NOESISTEX_DXT5
    #DXT5 packed normal map
    elif imgFmt == 4:
        data = rapi.imageUntile360DXT(rapi.swapEndianArray(data, 2), imgWidth, imgHeight, 16)
        data = rapi.imageDecodeDXT(data, imgWidth, imgHeight, noesis.FOURCC_ATI2)
        texFmt = noesis.NOESISTEX_RGBA32
    #DXT5 packed normal map2
    elif imgFmt == 5:
        data = rapi.imageUntile360DXT(rapi.swapEndianArray(data, 2), imgWidth, imgHeight, 16)
        data = rapi.imageDecodeDXT(data, imgWidth, imgHeight, noesis.FOURCC_ATI1)
        texFmt = noesis.NOESISTEX_RGBA32
    #DXT1 packed normal map
    elif imgFmt == 6:
        data = rapi.imageUntile360DXT(rapi.swapEndianArray(data, 2), imgWidth, imgHeight, 8)
        data = rapi.imageDecodeDXT(data, imgWidth, imgHeight, noesis.FOURCC_DXT1NORMAL)
        texFmt = noesis.NOESISTEX_RGBA32
    #raw
    elif imgFmt == 7:
        data = rapi.imageUntile360Raw(data, imgWidth, imgHeight, 4)
        data = rapi.imageDecodeRaw(data, imgWidth, imgHeight, "a8r8g8b8")
        texFmt = noesis.NOESISTEX_RGBA32
    #unknown, not handled
    else:
        print("WARNING: Unhandled image format")
        return None
    texList.append(NoeTexture(rapi.getInputName(), imgWidth, imgHeight, data, texFmt))
    return 1