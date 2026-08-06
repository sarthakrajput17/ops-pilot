from io import BytesIO

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)


def generate_pdf(analysis):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "<b>Ops-Pilot AI Report</b>",
            styles["Title"],
        )
    )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            f"Production Score: {analysis.score}/100",
            styles["Heading2"],
        )
    )

    elements.append(
        Paragraph(
            f"Overall Grade: {analysis.grade}",
            styles["Heading2"],
        )
    )

    elements.append(
        Paragraph(
            f"Risk Level: {analysis.risk}",
            styles["Heading2"],
        )
    )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            "<b>AI Summary</b>",
            styles["Heading1"],
        )
    )

    elements.append(
        Paragraph(
            analysis.summary,
            styles["BodyText"],
        )
    )

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            "<b>Validation Findings</b>",
            styles["Heading1"],
        )
    )

    for item in analysis.validation_issues:

        elements.append(
            Paragraph(
                f"""
                <b>{item.rule_id}</b><br/>
                Severity: {item.severity}<br/>
                Issue: {item.title}<br/>
                Recommendation: {item.recommendation}
                """,
                styles["BodyText"],
            )
        )

        elements.append(Spacer(1, 10))

    elements.append(Spacer(1, 20))

    elements.append(
        Paragraph(
            "<b>AI Recommendations</b>",
            styles["Heading1"],
        )
    )

    for rec in analysis.recommendations:

        elements.append(
            Paragraph(
                "• " + rec,
                styles["BodyText"],
            )
        )

    doc.build(elements)

    buffer.seek(0)

    return buffer