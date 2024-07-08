import pandas as pd

def df_to_html(df):
    """Converts a DataFrame into HTML with specific formatting."""
    html = "<table>"
    for _, row in df.iterrows():  # Iterate through rows
        country = row["Country"]
        visa = row["Visa requirement"]
        stay = row["Allowed stay"]
        notes = row["Notes (excluding departure fees)"]

        html += f"""
        <tr>
            <td><h3>{country}</h3></td> 
            <td>
                <p>
                    <b>Visa requirement:</b> {visa}<br>
                    <b>Allowed stay:</b> {stay}<br>
                    <b>Notes:</b> {notes}
                </p>
            </td>
        </tr>
        """
    html += "</table>"
    return html


# Assuming your DataFrame is named 'df'
html_output = df_to_html(df)

# Print or save the HTML
print(html_output)

# Optionally, save to a file
with open("visa_requirements.html", "w") as f:
    f.write(html_output)
