import json
import dash_table
import dash_html_components as html
import dash_core_components as dcc


def generate_data_table(self, summary, target):
        column_names = self.replace_col_names(summary[0], target)
        # slice column names array with the number of cols to be shown by default
        default_columns = []
        column_data = summary[1:]
        table_div = html.Div(self.build_category_data_table(column_names, default_columns,
                                                                     column_data, target))

        return html.Div(
            children=html.Div([
                table_div
            ]))



  def build_category_data_table(self,column_names,
                                  default_columns, column_data,
                                  target):

        column_data = self.remove(column_data, target)
        table_json = self.create_json_format(
            column_names, column_data)

        dropdown_div = dcc.Dropdown(id='data-table-dropdown-', value=default_columns,
                         multi=True,
                         clearable=False,
                         options=[{'label': self.capitalize_word(i), 'value': i}
                                  for i in column_names])

        table_container_div = html.Div(className="table-container", children=[
                dash_table.DataTable(
                    id='datatable',
                    columns=[
                        {"name": self.capitalize_word(i), "id": i} for i in default_columns
                    ],
                    data=table_json.to_dict("rows"),
                    sorting=False,
                    sorting_type="multi"
                )])

        return html.Div([dropdown_div, table_container_div])
