from app import dash_app


def test_header_present():
    layout = dash_app.layout
    ids = [component.id for component in layout.children if hasattr(component, "id")]
    assert "header" in ids


def test_visualization_present():
    layout = dash_app.layout
    ids = [component.id for component in layout.children if hasattr(component, "id")]
    assert "visualization" in ids


def test_region_picker_present():
    layout = dash_app.layout
    ids = [component.id for component in layout.children if hasattr(component, "id")]
    assert "region_picker" in ids