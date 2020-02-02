
import os


# https://nam03.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1_nvZklsTNOyqtpKYrZAvWZaoY0IJ51Hu%2Fview%3Fusp%3Dsharing&data=02%7C01%7C%7C0c9309a8fe0748a94d1a08d799173bce%7C17dcec9166ec4c4ba988473694df546c%7C1%7C0%7C637146197381549375&sdata=Oetmn948i9OUeklbbrqpG42O1lEkh7MFqNPDdRvxFCA%3D&reserved=0

def reverse(strs):
    return strs[4:8] + strs[2:4] + strs[0:2]


def main():

    for filename in os.listdir("C:/Users/siddh/Desktop/renameFile/"):
        dst = filename.replace(filename[-12:-4:1], reverse(filename[-12:-4:1]))
        # dst = "FCS_PLAN DATA_" + reverse("13012020") + ".eml"
        src = 'C:/Users/siddh/Desktop/renameFile/' + filename
        dst = 'C:/Users/siddh/Desktop/renameFile/' + dst

        os.rename(src, dst)


if __name__ == '__main__':

    main()
