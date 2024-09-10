import mesop as me
from ai.common.producer import producer_store as store
from ai.console.scaffold import page_scaffold


def on_load(e: me.LoadEvent):
  me.set_theme_mode("system")


@me.page(
  title="Mesop AI Console - Producers", path="/producers", on_load=on_load
)
def producers_page():
  with page_scaffold(current_path="/producers", title="Producers"):
    producers = store.get_all()
    with me.box(
      style=me.Style(
        display="grid",
        grid_template_columns="repeat(5, 1fr)",
        gap=16,
        align_items="center",
      )
    ):
      # Header
      me.text("ID", style=me.Style(font_weight="bold"))
      me.text("Model", style=me.Style(font_weight="bold"))
      me.text("Prompt Context", style=me.Style(font_weight="bold"))
      me.text("Output Format", style=me.Style(font_weight="bold"))
      me.text("Temperature", style=me.Style(font_weight="bold"))
      # Body
      for producer in producers:
        me.button(
          producer.id,
          on_click=lambda e: me.navigate(
            "/producers/edit", query_params={"id": e.key}
          ),
          key=producer.id,
          style=me.Style(font_size=16),
        )
        me.button(
          producer.mesop_model_id,
          on_click=lambda e: me.navigate(
            "/models/edit", query_params={"id": e.key}
          ),
          key=producer.mesop_model_id,
          style=me.Style(font_size=16),
        )
        me.button(
          producer.prompt_context_id,
          on_click=lambda e: me.navigate(
            "/prompt-contexts/edit", query_params={"id": e.key}
          ),
          key=producer.prompt_context_id,
          style=me.Style(font_size=16),
        )
        me.text(producer.output_format)
        me.text(str(producer.temperature))
    with me.box(style=me.Style(padding=me.Padding(top=32))):
      me.button(
        "Add Producer",
        on_click=lambda e: me.navigate("/producers/add"),
        type="flat",
        color="accent",
      )
