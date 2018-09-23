from webscanners.models import acunetix_scan_db, acunetix_scan_result_db
import uuid
import hashlib

ScanName = None
ScanShortName = None
ScanStartURL = None
ScanStartTime = None
ScanFinishTime = None
ScanScanTime = None
ScanAborted = None
ScanResponsive = None
ScanBanner = None
ScanOs = None
ScanWebServer = None
ScanTechnologies = None
ScanCrawler = None
ScanReportItems = None
VulnName = None
VulnModuleName = None
VulnDetails = None
VulnAffects = None
VulnParameter = None
VulnAOP_SourceFile = None
VulnAOP_SourceLine = None
VulnAOP_Additional = None
VulnIsFalsePositive = None
VulnSeverity = None
VulnType = None
VulnImpact = None
VulnDescription = None
VulnDetailedInformation = None
VulnRecommendation = None
VulnTechnicalDetails = None
VulnCWEList = None
VulnCVEList = None
VulnCVSS = None
VulnCVSS3 = None
VulnReferences = None
vul_col = None
risk = None
UriName = None
VulnUrl = None
FullURL = None


def xml_parser(root, project_id, scan_id):
    """

    :param root:
    :param project_id:
    :param scan_id:
    :return:
    """
    global ScanName, \
        ScanShortName, ScanStartURL, \
        ScanStartTime, \
        ScanFinishTime, \
        ScanScanTime, \
        ScanAborted, \
        ScanResponsive, \
        ScanResponsive, \
        ScanBanner, \
        ScanOs, \
        ScanWebServer, \
        ScanTechnologies, \
        ScanCrawler, \
        ScanReportItems, \
        VulnName, \
        VulnModuleName, \
        VulnDetails, \
        VulnAffects, \
        VulnParameter, \
        VulnAOP_SourceFile, \
        VulnAOP_SourceLine, \
        VulnAOP_Additional, \
        VulnIsFalsePositive, \
        VulnSeverity, \
        VulnType, \
        VulnImpact, \
        VulnDescription, \
        VulnDetailedInformation, \
        VulnRecommendation, \
        VulnTechnicalDetails, \
        VulnCWEList, \
        VulnCVEList, \
        VulnCVSS, \
        VulnCVSS3, \
        VulnReferences, \
        vul_col, \
        risk, \
        UriName, \
        VulnUrl, \
        FullURL

    for scan in root:
        for reports in scan:
            if reports.tag == 'Name':
                ScanName = reports.text
                print "scanname---", ScanName
            if reports.tag == 'ShortName':
                ScanShortName = reports.text
            if reports.tag == 'StartURL':
                ScanStartURL = reports.text
                print 'scan_start_url-----', ScanStartURL
            if reports.tag == 'StartTime':
                ScanStartTime = reports.text
            if reports.tag == 'FinishTime':
                ScanFinishTime = reports.text
            if reports.tag == 'ScanTime':
                ScanScanTime = reports.text
            if reports.tag == 'Aborted':
                ScanAborted = reports.text
            if reports.tag == 'Responsive':
                ScanResponsive = reports.text
            if reports.tag == 'Banner':
                ScanBanner = reports.text
            if reports.tag == 'Os':
                ScanOs = reports.text
            if reports.tag == 'WebServer':
                ScanWebServer = reports.text
            if reports.tag == 'Technologies':
                ScanTechnologies = reports.text
            if reports.tag == 'Crawler':
                ScanCrawler = reports.text
            if reports.tag == 'ReportItems':
                ScanReportItems = reports.text
            if reports.tag == 'ReportItems':
                ScanReportItems = reports.text
            for report_item in reports:
                for ReportItem in report_item:
                    # print ReportItem
                    # print(ReportItem.tag)

                    if ReportItem.tag == 'Name':
                        VulnName = ReportItem.text
                        print VulnName

                    if ReportItem.tag == 'ModuleName':
                        VulnModuleName = ReportItem.text

                    if ReportItem.tag == 'Details':
                        VulnDetails = ReportItem.text

                    if ReportItem.tag == 'Affects':
                        VulnAffects = ReportItem.text

                    if ReportItem.tag == 'Parameter':
                        VulnParameter = ReportItem.text

                    if ReportItem.tag == 'AOP_SourceFile':
                        VulnAOP_SourceFile = ReportItem.text

                    if ReportItem.tag == 'AOP_SourceLine':
                        VulnAOP_SourceLine = ReportItem.text

                    if ReportItem.tag == 'AOP_Additional':
                        VulnAOP_Additional = ReportItem.text

                    if ReportItem.tag == 'IsFalsePositive':
                        VulnIsFalsePositive = ReportItem.text

                    if ReportItem.tag == 'Severity':
                        VulnSeverity = ReportItem.text

                    if ReportItem.tag == 'Type':
                        VulnType = ReportItem.text

                    if ReportItem.tag == 'Impact':
                        VulnImpact = ReportItem.text

                    if ReportItem.tag == 'Description':
                        VulnDescription = ReportItem.text

                    if ReportItem.tag == 'DetailedInformation':
                        VulnDetailedInformation = ReportItem.text

                    if ReportItem.tag == 'Recommendation':
                        VulnRecommendation = ReportItem.text

                    if ReportItem.tag == 'TechnicalDetails':
                        VulnTechnicalDetails = ReportItem.text

                    if ReportItem.tag == 'CWEList':
                        VulnCWEList = ReportItem.text

                    if ReportItem.tag == 'CVEList':
                        VulnCVEList = ReportItem.text

                    if ReportItem.tag == 'CVSS':
                        VulnCVSS = ReportItem.text

                    if ReportItem.tag == 'CVSS3':
                        VulnCVSS3 = ReportItem.text

                    if ReportItem.tag == 'References':
                        VulnReferences = ReportItem.text

                    if VulnSeverity == "high":
                        vul_col = "important"
                        risk = "High"
                    elif VulnSeverity == 'medium':
                        vul_col = "warning"
                        risk = "Medium"
                    elif VulnSeverity == 'low':
                        vul_col = "info"
                        risk = "Low"
                    elif VulnSeverity == 'informational':
                        vul_col = "info"
                        risk = "Informational"

                for c_url in root.findall('.//SiteFile'):
                    for vuln_url in c_url:
                        if vuln_url.tag == 'Name':
                            UriName = vuln_url.text
                        if vuln_url.tag == 'URL':
                            VulnUrl = vuln_url.text
                        if vuln_url.tag == 'FullURL':
                            FullURL = vuln_url.text

                vuln_id = uuid.uuid4()
                # print VulnName, ScanStartURL, VulnSeverity
                dup_data = str(VulnName) + str(ScanStartURL) + str(VulnSeverity)
                duplicate_hash = hashlib.sha1(dup_data).hexdigest()
                match_dup = acunetix_scan_result_db.objects.filter(
                    dup_hash=duplicate_hash).values('dup_hash').distinct()
                lenth_match = len(match_dup)

                if lenth_match == 1:
                    duplicate_vuln = 'Yes'
                elif lenth_match == 0:
                    duplicate_vuln = 'No'
                else:
                    duplicate_vuln = 'None'

                false_p = acunetix_scan_result_db.objects.filter(
                    false_positive_hash=duplicate_hash)
                fp_lenth_match = len(false_p)

                if fp_lenth_match == 1:
                    false_positive = 'Yes'
                else:
                    false_positive = 'No'

                dump_data = acunetix_scan_result_db(
                    scan_id=scan_id,
                    project_id=project_id,
                    vuln_id=vuln_id,
                    false_positive=false_positive,
                    vuln_color=vul_col,
                    vuln_status='Open',
                    dup_hash=duplicate_hash,
                    vuln_duplicate=duplicate_vuln,
                    ScanName=ScanName,
                    ScanShortName=ScanShortName,
                    ScanStartURL=ScanStartURL,
                    ScanStartTime=ScanStartTime,
                    ScanFinishTime=ScanFinishTime,
                    ScanScanTime=ScanScanTime,
                    ScanAborted=ScanAborted,
                    ScanResponsive=ScanResponsive,
                    ScanBanner=ScanBanner,
                    ScanOs=ScanOs,
                    ScanWebServer=ScanWebServer,
                    ScanTechnologies=ScanTechnologies,
                    ScanCrawler=ScanCrawler,
                    ScanReportItems=ScanReportItems,
                    VulnName=VulnName,
                    VulnModuleName=VulnModuleName,
                    VulnDetails=VulnDetails,
                    VulnAffects=VulnAffects,
                    VulnParameter=VulnParameter,
                    VulnAOP_SourceFile=VulnAOP_SourceFile,
                    VulnAOP_SourceLine=VulnAOP_SourceLine,
                    VulnAOP_Additional=VulnAOP_Additional,
                    VulnIsFalsePositive=VulnIsFalsePositive,
                    VulnSeverity=risk,
                    VulnType=VulnType,
                    VulnImpact=VulnImpact,
                    VulnDescription=VulnDescription,
                    VulnDetailedInformation=VulnDetailedInformation,
                    VulnRecommendation=VulnRecommendation,
                    VulnTechnicalDetails=VulnTechnicalDetails,
                    VulnCWEList=VulnCWEList,
                    VulnCVEList=VulnCVEList,
                    VulnCVSS=VulnCVSS,
                    VulnCVSS3=VulnCVSS3,
                    VulnReferences=VulnReferences,
                    UriName=UriName,
                    VulnUrl=VulnUrl,
                    VulnFullUrl=FullURL

                )
                dump_data.save()

    acunetix_all_vul = acunetix_scan_result_db.objects.filter(scan_id=scan_id) \
        .values('VulnName', 'VulnSeverity', 'vuln_color', 'vuln_duplicate').distinct()

    total_vul = len(acunetix_all_vul)
    total_high = len(acunetix_all_vul.filter(VulnSeverity="High"))
    total_medium = len(acunetix_all_vul.filter(VulnSeverity="Medium"))
    total_low = len(acunetix_all_vul.filter(VulnSeverity="Low"))
    total_duplicate = len(acunetix_all_vul.filter(vuln_duplicate='Yes'))

    acunetix_scan_db.objects.filter(scan_id=scan_id) \
        .update(total_vul=total_vul,
                high_vul=total_high,
                medium_vul=total_medium,
                low_vul=total_low,
                total_dup=total_duplicate
                )
    if total_vul == total_duplicate:
        acunetix_scan_db.objects.filter(scan_id=scan_id) \
            .update(total_vul='0',
                    high_vul='0',
                    medium_vul='0',
                    low_vul='0',
                    total_dup=total_duplicate
                    )
