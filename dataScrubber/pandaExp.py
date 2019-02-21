
import ds3
import ds5 
import ds6
import ds8
import ds10
import ds11
import ds12
import ds13
import ds14
import ds15

print("Instant Noodles!")




# these are note that you can ignore :] this file runs all the other files so you can have instant noodles


# acct = '4121-0211-3911-0061'

# print(acct[0:4]) #first set of 4
# print(acct[5:9]) #sec set of 4
# print(acct[10:14]) #third set of 4
# print(acct[15:19]) #forth set of 4

# phone = '407-744-7393'

# print(phone[0:3]) #first
# print(phone[4:7]) #sec 
# print(phone[8:12]) #third

#Each character in a string including white space counts, 
# First number inside index brackets is where the indexing starts
# Secound number inside index brackets is where the indexing ends
# Starting and ending points are not included in what is returned.

    # def runx(self, add_days=900, nrpt="MPP_RECEIPT_ADJ.TXT"):
    #     """
    #     Scrubs file adding add_days to the record dates to fudge multiple versions
    #     :param add_days: number of days to add to individual record (line item) dates
    #     :param nrpt:
    #     :return:
    #     """
    #     RX = r'.{61}\d{2}\/\d{2}\/\d{2} \d{2}\/\d{2}\/\d{2}'
    #     RX2 = r'SOME PARK HOSPITALS'
    #     RX3 = r'HOSPITAL \d{2} \( .{8} \)'
    #     RX4 = r'\(.{10}\)'
    #     RXDATE = r'(?P<date>\d{2}\/\d{2}\/\d{2})'

    #     demo_file = 'rpt_sources/MPP_RECEIPT_ADJ.TXT' #... the 'ARX4T.TXT'

    #     with open(demo_file, 'r') as fupd:
    #         """
    #         read the demo_file - the source file to be scrubbed
    #         nrpt is where the new (scrubbed) file lines will be stored
    #         """
    #         with open(nrpt, 'w') as fout:  #open the output file in write mode
    #             while True:
    #                 sline = fupd.readline()

    #                 if not sline: break
    #                 nline = io.StringIO(sline)
    #                 for mo in re.finditer(RXDATE, sline):
    #                     _x = mo.start('date')
    #                     ddate = datetime.strptime(mo.group('date'), '%m/%d/%y')
    #                     nline.seek(_x)
    #                     nline.write((ddate + timedelta(days=add_days)).strftime('%m/%d/%y'))
    #                 sline = nline.getvalue()