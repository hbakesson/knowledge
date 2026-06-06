import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

# Colors
NAVY = RGBColor(15, 23, 42)       # Slate 900 (#0F172A)
SLATE = RGBColor(71, 85, 105)     # Slate 600 (#475569)
CHARCOAL = RGBColor(51, 65, 85)   # Slate 700 (#334155)
LIGHT_BG = "F1F5F9"               # Slate 100 (#F1F5F9)

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('w:top', top), ('w:bottom', bottom), ('w:left', left), ('w:right', right)]:
        node = OxmlElement(m)
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def add_bottom_border(paragraph, hex_color="0F172A", size="12"):
    pPr = paragraph._p.get_or_add_pPr()
    pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="{size}" w:space="4" w:color="{hex_color}"/></w:pBdr>')
    pPr.append(pBdr)

def apply_text_styling(run, font_name="Calibri", size_pt=11, color=CHARCOAL, bold=False, italic=False):
    run.font.name = font_name
    run.font.size = Pt(size_pt)
    run.font.color.rgb = color
    run.bold = bold
    run.italic = italic

def set_margins(doc):
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.9)
        section.right_margin = Inches(0.9)

def create_cv():
    doc = Document()
    set_margins(doc)
    
    # 1. Header Name
    p_name = doc.add_paragraph()
    p_name.paragraph_format.space_before = Pt(0)
    p_name.paragraph_format.space_after = Pt(4)
    run_name = p_name.add_run("Sofia Sjöqvist")
    apply_text_styling(run_name, "Georgia", 26, NAVY, bold=True)
    
    # Header Subtitle/Title
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_after = Pt(8)
    run_title = p_title.add_run("DORA Compliance Manager")
    apply_text_styling(run_title, "Calibri", 13, SLATE, bold=True, italic=True)
    
    # Contact Info line
    p_contact = doc.add_paragraph()
    p_contact.paragraph_format.space_after = Pt(20)
    p_contact.paragraph_format.line_spacing = 1.15
    add_bottom_border(p_contact, "E2E8F0", "6") # Thin divider line
    
    contact_text = "Malmö / Stockholm  |  +46 70 000 00 00  |  sofia.sjoqvist@email.com  |  linkedin.com/in/sofia-sjoqvist"
    run_contact = p_contact.add_run(contact_text)
    apply_text_styling(run_contact, "Calibri", 9.5, SLATE)

    # 2. Profile Callout Box
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.cell(0, 0)
    set_cell_background(cell, LIGHT_BG)
    set_cell_margins(cell, top=140, bottom=140, left=200, right=200)
    
    # Set borders of the callout cell: Left border navy, others none
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:top w:val="none"/>'
        f'<w:left w:val="single" w:sz="36" w:color="0F172A"/>'
        f'<w:bottom w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(tcBorders)
    
    p_prof_head = cell.paragraphs[0]
    p_prof_head.paragraph_format.space_after = Pt(4)
    run_ph = p_prof_head.add_run("PROFIL")
    apply_text_styling(run_ph, "Calibri", 10.5, NAVY, bold=True)
    
    p_prof_body = cell.add_paragraph()
    p_prof_body.paragraph_format.space_after = Pt(0)
    p_prof_body.paragraph_format.line_spacing = 1.15
    prof_text = (
        "Erfaren, affärsorienterad och trygg ledare inom compliance, riskhantering och IKT-styrning "
        "med över 20 års erfarenhet från finansiella och regulatoriskt tillsynade verksamheter. Genom att "
        "ha arbetat i samtliga tre försvarslinjer – som extern/internrevisor, IT-avdelningschef samt "
        "Compliance Officer – har jag en unik förmåga att översätta komplexa lagkrav till praktisk och "
        "effektiv IKT-styrning.\n\n"
        "Jag har djupgående erfarenhet av att leda förändringsarbete och implementera regulatoriska "
        "ramverk såsom DORA (med särskilt fokus på IKT-tredjepartsrisker och incidenthantering) samt "
        "Solvens II. Som ledare är jag känd för att bygga broar mellan affärsverksamhet, IT-säkerhet "
        "och juridik för att stärka den digitala operativa motståndskraften och skapa genuint affärsvärde."
    )
    run_pb = p_prof_body.add_run(prof_text)
    apply_text_styling(run_pb, "Calibri", 10, CHARCOAL)
    
    # Spacer
    p_space = doc.add_paragraph()
    p_space.paragraph_format.space_before = Pt(12)
    p_space.paragraph_format.space_after = Pt(0)
    
    # Helper to add section headers
    def add_section_header(title):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(18)
        p.paragraph_format.space_after = Pt(8)
        add_bottom_border(p, "0F172A", "12") # Thicker border
        r = p.add_run(title)
        apply_text_styling(r, "Georgia", 14, NAVY, bold=True)
        return p

    # 3. Nyckelkompetenser
    add_section_header("NYCKELKOMPETENSER")
    
    competences = [
        ("DORA & IKT-riskstyrning", "Djup expertis i implementering av DORA-ramverket, inklusive hantering av tredje parts IKT-risk, avtalskrav, IKT-incidentrapportering samt penetrations- och sårbarhetstester."),
        ("IKT-styrning & IT-säkerhet", "Flerårig erfarenhet som IT-chef med ansvar för system, budget och operativ motståndskraft."),
        ("Regelefterlevnad (Compliance)", "Självständig granskning, rådgivning och rapportering direkt till VD, ledningsgrupp och styrelse inom tillsynade verksamheter (Folksam, Riksbanken)."),
        ("Tredjepartshantering & Outsourcing", "Specialist på kravställning, riskbedömning och avtalsreglering vid utkontraktering av IT-tjänster (molntjänster, kritiska systemleverantörer)."),
        ("Förändringsledning & Samverkan", "Dokumenterad förmåga att driva tvärfunktionella projekt och hantera intressenter (stakeholders) på alla nivåer i komplexa organisationer.")
    ]
    
    for title, desc in competences:
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        r_title = p.add_run(title + ": ")
        apply_text_styling(r_title, "Calibri", 10, NAVY, bold=True)
        r_desc = p.add_run(desc)
        apply_text_styling(r_desc, "Calibri", 10, CHARCOAL)

    # 4. Arbetslivserfarenhet
    add_section_header("ARBETSLIVSERFARENHET")
    
    jobs = [
        {
            "role": "Compliance Officer",
            "company": "Folksam",
            "period": "Maj 2025 – Pågående",
            "points": [
                "Ansvarig för oberoende granskning, riskbaserad uppföljning och rådgivning avseende regelefterlevnad inom försäkring och tjänstepension.",
                "**Särskilt DORA-fokus:** Har under det senaste året drivit Folksams anpassning till DORA med särskilt fokus på IKT-tredjepartsrisker, granskning av kritiska leverantörsavtal, analys av koncentrationsrisker samt upprättande av informationsregister för finansiella enheter.",
                "Löpande rådgivning till VD, företagsledning och styrelse kring regulatoriska risker samt samverkan med risk- och IT-säkerhetsfunktioner."
            ]
        },
        {
            "role": "Avdelningschef IT",
            "company": "Folksam",
            "period": "2018 – 2025",
            "points": [
                "Personal-, system- och budgetansvar för tvärfunktionella utvecklingsteam (10–15 personer) fokuserade på boksluts- och myndighetsrapportering till Finansinspektionen och EIOPA.",
                "**DORA-implementering (2024):** Ledde det operativa arbetet för att stärka IT-säkerheten, sårbarhetshanteringen och den digitala återställningsförmågan i enlighet med DORA.",
                "Etablerade Folksams RPA-team (Robotic Process Automation) som framgångsrikt automatiserade kritiska processer och reducerade operativ risk."
            ]
        },
        {
            "role": "Verksamhetsutvecklare (Ekonomi & Finans)",
            "company": "Folksam",
            "period": "2013 – 2018",
            "points": [
                "Nyckelroll i det företagsövergripande programmet för införande av Solvens II med fokus på pelare 2 (intern styrning och kontroll, ORSA).",
                "Ansvarig för ekonomi- och finansavdelningens risk- och regelefterlevnadsarbete i nära samarbete med den centrala risk- och compliancefunktionen.",
                "Kontinuitetsansvarig (BCP/DR) samt delaktig i upphandling och kravställning av externa revisions- och IT-tjänster."
            ]
        },
        {
            "role": "Internrevisor",
            "company": "Folksam (Koncernstaben)",
            "period": "2012 – 2013",
            "points": [
                "Reviderade och utvärderade Folksams kapitalförvaltning samt risk- och compliancefunktioner.",
                "Ansvarig för utveckling och kvalitetssäkring av revisionsmetodiken enligt god revisionssed."
            ]
        },
        {
            "role": "Internrevisor",
            "company": "Sveriges Riksbank",
            "period": "2008 – 2012",
            "points": [
                "Ansvarig för revisionsmetodik och samordning av internationellt revisionssamarbete med Europeiska Centralbanken (ECB) i Frankfurt.",
                "Drivande i uppstarts- och rådgivningsarbetet för etableringen av en ny internrevisionsfunktion på Finansinspektionen."
            ]
        },
        {
            "role": "Externrevisor & Konsult",
            "company": "Deloitte",
            "period": "2000 – 2008",
            "points": [
                "Granskning, rådgivning och kvalitetssäkring inom risk, compliance och internrevision för ledande aktörer inom bank och försäkring.",
                "Tf. gruppchef inom internrevisionen på ett av Sveriges största livförsäkringsbolag.",
                "Internationell erfarenhet genom tjänstgöring i New York."
            ]
        }
    ]
    
    for job in jobs:
        p_job = doc.add_paragraph()
        p_job.paragraph_format.space_before = Pt(8)
        p_job.paragraph_format.space_after = Pt(2)
        
        # We put Role, Company and Period on a single line or two lines.
        r_role = p_job.add_run(job["role"])
        apply_text_styling(r_role, "Calibri", 11, NAVY, bold=True)
        
        r_sep = p_job.add_run("  |  ")
        apply_text_styling(r_sep, "Calibri", 11, SLATE)
        
        r_comp = p_job.add_run(job["company"])
        apply_text_styling(r_comp, "Calibri", 11, CHARCOAL, bold=True)
        
        r_space = p_job.add_run(" " * 6)
        apply_text_styling(r_space, "Calibri", 11, SLATE)
        
        r_per = p_job.add_run(job["period"])
        apply_text_styling(r_per, "Calibri", 10.5, SLATE, italic=True)
        
        for pt in job["points"]:
            p_pt = doc.add_paragraph(style='List Bullet')
            p_pt.paragraph_format.space_after = Pt(3)
            p_pt.paragraph_format.line_spacing = 1.15
            
            # Simple bold parser for markdown style **bold**
            parts = pt.split("**")
            is_bold = False
            for part in parts:
                r_pt = p_pt.add_run(part)
                apply_text_styling(r_pt, "Calibri", 10, CHARCOAL, bold=is_bold)
                is_bold = not is_bold

    # 5. Utbildning & Certifieringar
    add_section_header("UTBILDNING & CERTIFIERINGAR")
    
    certs = [
        ("Magisterexamen i företagsekonomi", "Handelshögskolan vid Göteborgs universitet, 2000"),
        ("Certifierad Internrevisor (CIA)", "IIA Sweden, 2008–2013"),
        ("Outsourcing inom försäkring", "Utbildning via Svensk Försäkringsförening (SFF), 2025"),
        ("Tuff Ledarskapsutbildning (Steg 1 & 2) samt The Human Element", "2022–2024")
    ]
    
    for title, detail in certs:
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        r_t = p.add_run(title)
        apply_text_styling(r_t, "Calibri", 10, CHARCOAL, bold=True)
        r_d = p.add_run(" – " + detail)
        apply_text_styling(r_d, "Calibri", 10, CHARCOAL)

    doc.save("cv_fortnox.docx")

def create_letter():
    doc = Document()
    set_margins(doc)
    
    # Header Name
    p_name = doc.add_paragraph()
    p_name.paragraph_format.space_before = Pt(0)
    p_name.paragraph_format.space_after = Pt(4)
    run_name = p_name.add_run("Sofia Sjöqvist")
    apply_text_styling(run_name, "Georgia", 26, NAVY, bold=True)
    
    # Contact Info line
    p_contact = doc.add_paragraph()
    p_contact.paragraph_format.space_after = Pt(24)
    add_bottom_border(p_contact, "E2E8F0", "6")
    
    contact_text = "Malmö / Stockholm  |  +46 70 000 00 00  |  sofia.sjoqvist@email.com  |  linkedin.com/in/sofia-sjoqvist"
    run_contact = p_contact.add_run(contact_text)
    apply_text_styling(run_contact, "Calibri", 9.5, SLATE)
    
    # Metadata info (Date and To)
    p_meta = doc.add_paragraph()
    p_meta.paragraph_format.space_after = Pt(16)
    r_meta = p_meta.add_run("Till: Fortnox Finans AB\nSökt tjänst: DORA Compliance Manager\nDatum: 6 juni 2026")
    apply_text_styling(r_meta, "Calibri", 10.5, SLATE, italic=True)
    
    # Title
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_after = Pt(14)
    r_title = p_title.add_run("Ansökan: DORA Compliance Manager")
    apply_text_styling(r_title, "Georgia", 16, NAVY, bold=True)
    
    # Body text paragraphs
    body_paragraphs = [
        "Hej,",
        
        "Jag blev mycket glad när jag såg er annons för rollen som DORA Compliance Manager. Att kombinera strikt regelefterlevnad med praktisk och affärsnära IKT-styrning är precis vad min yrkesbana har handlat om de senaste åren. Jag har följt Fortnox framgångsresa och attraheras starkt av er kultur av innovation, enkelhet och att ligga i teknisk framkant. Jag är övertygad om att jag kan bidra till att säkra Fortnox Finans AB:s digitala operativa motståndskraft på ett sätt som inte bara uppfyller lagkrav, utan också stärker er affär.",
        
        "Under det senaste året har jag i min roll som Compliance Officer på Folksam fokuserat intensivt på DORA-förordningen. Mina insatser har framför allt legat inom IKT-tredjepartsrisk och outsourcing – områden som är helt avgörande för ett teknikdrivet bolag som Fortnox Finans. Jag har lett arbetet med att analysera och anpassa våra leverantörsavtal, kartlägga koncentrationsrisker samt bygga upp strukturen för IKT-informationsregistret.",
        
        "Min unika styrka är att jag förstår DORA från flera olika perspektiv:",
        
        "1. IT och det operativa perspektivet: Som tidigare IT-avdelningschef på Folksam under sju år förstår jag systemarkitektur, utvecklingsteamens vardag och vad som krävs för att omsätta säkerhetskrav i praktiken utan att bromsa utvecklingstakten.",
        
        "2. Compliance och styrningsperspektivet: Som Compliance Officer och före detta internrevisor (bland annat på Riksbanken och Folksam) har jag stor vana vid att självständigt tolka lagkrav, designa kontrollfunktioner och rapportera direkt till VD, ledningsgrupp och styrelse.",
        
        "3. Tillsynsperspektivet: Genom mitt tidigare arbete med att etablera en ny internrevisionsfunktion på Finansinspektionen samt mitt samarbete med Europeiska Centralbanken (ECB), har jag en god förståelse för tillsynsmyndigheternas förväntningar och hur man för en konstruktiv dialog med dem.",
        
        "I rollen som DORA Compliance Manager hos er ser jag mig själv som en möjliggörare. DORA handlar inte bara om att bocka av checklistor; rätt implementerat skapar det färre driftstopp, högre driftsäkerhet, bättre kontroll över leverantörer och – framför allt – ett ännu starkare förtroende från era kunder och samarbetspartners.",
        
        "Jag trivs i miljöer där man uppmuntras att ta initiativ, samarbeta tvärs över gränser och driva ständiga förbättringar. Jag är en pedagogisk kommunikatör som trivs lika bra med att diskutera tekniska detaljer med IT-säkerhetsavdelningen som att presentera strategiska risker för styrelsen.",
        
        "Jag ser fram emot att berätta mer om hur mina erfarenheter och mitt engagemang kan bidra till Fortnox fortsatta framgångar.",
        
        "Med vänliga hälsningar,\n\nSofia Sjöqvist"
    ]
    
    for text in body_paragraphs:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(10)
        p.paragraph_format.line_spacing = 1.15
        
        # Styling lists in the body paragraphs
        if text.startswith("1.") or text.startswith("2.") or text.startswith("3."):
            prefix, rest = text.split(":", 1)
            r_pre = p.add_run(prefix + ":")
            apply_text_styling(r_pre, "Calibri", 10.5, NAVY, bold=True)
            r_rest = p.add_run(rest)
            apply_text_styling(r_rest, "Calibri", 10.5, CHARCOAL)
            p.paragraph_format.left_indent = Inches(0.25)
        else:
            r = p.add_run(text)
            apply_text_styling(r, "Calibri", 10.5, CHARCOAL)
            
    doc.save("brev_fortnox.docx")

if __name__ == "__main__":
    create_cv()
    create_letter()
    print("Files created successfully.")
