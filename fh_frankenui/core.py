# AUTOGENERATED! DO NOT EDIT! File to edit: ../lib_nbs/01_core.ipynb.

# %% auto 0
__all__ = ['enum_to_markdown_table', 'fast_app', 'FastHTML', 'Theme', 'TextT', 'TextFont', 'ButtonT', 'Button', 'ButtonSubmit',
           'H1', 'H2', 'H3', 'H4', 'Main', 'Titled', 'DividerT', 'Divider', 'DividerSplit', 'DividerLine', 'Article',
           'ArticleTitle', 'ArticleMeta', 'ContainerT', 'Container', 'SectionT', 'Section', 'Fieldset', 'Legend',
           'Input', 'Select', 'Radio', 'CheckboxX', 'Range', 'Toggle_switch', 'TextArea', 'Switch', 'FormLabel',
           'LabelT', 'Label', 'UkFormSection', 'GenericLabelInput', 'LabelInput', 'LabelRadio', 'LabelCheckboxX',
           'LabelRange', 'LabelTextArea', 'LabelSwitch', 'LabelSelect', 'Options', 'UkSelect', 'LabelUkSelect', 'AT',
           'ListT', 'List', 'ModalContainer', 'ModalDialog', 'ModalHeader', 'ModalBody', 'ModalFooter', 'ModalTitle',
           'ModalCloseButton', 'Modal', 'PaddingT', 'PositionT', 'Placeholder', 'Progress', 'UkIcon', 'UkIconLink',
           'DiceBearAvatar', 'FlexT', 'Grid', 'DivFullySpaced', 'DivCentered', 'DivLAligned', 'DivRAligned',
           'DivVStacked', 'DivHStacked', 'NavT', 'NavContainer', 'NavParentLi', 'NavDividerLi', 'NavHeaderLi',
           'NavSubtitle', 'NavCloseLi', 'NavBarContainer', 'NavBarLSide', 'NavBarRSide', 'NavBarCenter', 'NavBarNav',
           'NavBarSubtitle', 'NavBarNavContainer', 'NavBarParentIcon', 'DropDownNavContainer', 'TabContainer', 'CardT',
           'CardTitle', 'CardHeader', 'CardBody', 'CardFooter', 'CardContainer', 'Card', 'TableT', 'Table', 'Td', 'Th',
           'Tr', 'Thead', 'Tbody', 'TableFromLists', 'TableFromDicts', 'apply_classes', 'render_md']

# %% ../lib_nbs/01_core.ipynb
import fasthtml.common as fh
from .foundations import *
from fasthtml.common import is_listy, Div, P, Span, Script, FastHTML, FT, to_xml, show,fast_app
from fasthtml.svg import Svg
from fasthtml.components import Uk_theme_switcher, Main

from enum import Enum, auto
from fasthtml.components import Uk_select,Uk_input_tag,Uk_icon
from functools import partial
from itertools import zip_longest
from typing import Union, Tuple, Optional
from fastcore.all import *
import copy, re


# %% ../lib_nbs/01_core.ipynb
def enum_to_markdown_table(enum_class):
    headers = ["Option", "Value"]
    rows = [[name, value.value] for name, value in enum_class.__members__.items()]
    
    max_name_len = max(len(row[0]) for row in rows)
    max_value_len = max(len(row[1]) for row in rows)
    
    header = f"| {'Option':<{max_name_len}} | {'Value':<{max_value_len}} |"
    separator = f"|{'-'*(max_name_len+2)}|{'-'*(max_value_len+2)}|"
    body = "\n".join(f"| {row[0]:<{max_name_len}} | {row[1]:<{max_value_len}} |" for row in rows)
    
    return f"{header}\n{separator}\n{body}"

# %% ../lib_nbs/01_core.ipynb
@delegates(fh.fast_app)
def fast_app(*args, **kwargs):
    "Adds `bg-background text-foreground` to bodykw for frankenui themes"
    if 'bodykw' not in kwargs: kwargs['bodykw'] = {}
    if 'class' not in kwargs['bodykw']: kwargs['bodykw']['class'] = ''
    kwargs['bodykw']['class'] = stringify((kwargs['bodykw']['class'],'bg-background text-foreground'))
    return fh.fast_app(*args, **kwargs)

# %% ../lib_nbs/01_core.ipynb
@delegates(fh.FastHTML)
def FastHTML(*args, **kwargs):
    "Adds `bg-background text-foreground` to bodykw for frankenui themes"
    if 'bodykw' not in kwargs: kwargs['bodykw'] = {}
    if 'bodykw' not in kwargs['bodykw']: kwargs['bodykw']['class'] = ''
    kwargs['bodykw']['class'] = stringify((kwargs['bodykw']['class'],'bg-background text-foreground'))
    return fh.FastHTML(*args, **kwargs)

# %% ../lib_nbs/01_core.ipynb
def _headers_theme(color):    
    return fh.Script(f'''const htmlElement = document.documentElement;
          if (
            localStorage.getItem("mode") === "dark" ||
            (!("mode" in localStorage) &&
              window.matchMedia("(prefers-color-scheme: dark)").matches)
          ) {{
            htmlElement.classList.add("dark");
          }} else {{
            htmlElement.classList.remove("dark");
          }}

          htmlElement.classList.add(localStorage.getItem("theme") || "uk-theme-{color}");
          ''')

# %% ../lib_nbs/01_core.ipynb
class Theme(Enum):
    "Selector to choose theme and get all headers needed for app.  Includes frankenui + tailwind"
    def _generate_next_value_(name, start, count, last_values): return name
    slate = auto()
    stone = auto()
    gray = auto()
    neutral = auto()
    red = auto()
    rose = auto()
    orange = auto()
    green = auto()
    blue = auto()
    yellow = auto()
    violet = auto()
    zinc = auto()
    
    def headers(self):
        return (fh.Link(rel="stylesheet", href="https://unpkg.com/franken-ui@1.1.0/dist/css/core.min.css"),
            fh.Script( type="module", src ="https://unpkg.com/franken-ui@1.1.0/dist/js/core.iife.js"),
            fh.Script( type="module", src ="https://unpkg.com/franken-ui@1.1.0/dist/js/icon.iife.js"),
            fh.Script(src="https://cdn.tailwindcss.com"),
            _headers_theme(self.value),)

# %% ../lib_nbs/01_core.ipynb
class TextT(VEnum):
    'Text Styles from https://franken-ui.dev/docs/text'
    def _generate_next_value_(name, start, count, last_values):
        return str2ukcls('text', name)
    
    # Text Style
    lead,meta, italic = auto(), auto(), auto()
    # Text Size
    small, default, large = auto(), 'uk-text', auto()
    # Text Weight
    light, normal, bold, lighter, bolder = auto(),auto(),auto(),auto(),auto()
    # Text Transform
    capitalize,uppercase, lowercase = auto(),auto(),auto()
    # Text Decoration
    decoration_none = auto()
    # Text Color
    muted,primary,secondary, success,warning, danger = auto(),auto(),auto(),auto(),auto(),auto()
    # Text Alignment
    left, right,center,justify = auto(), auto(), auto(), auto()
    # Vertical Alignment
    top,middle,bottom, baseline = auto(),auto(),auto(),auto()
    
    # Text Wrapping
    truncate,break_,nowrap = auto(),auto(),auto()

# %% ../lib_nbs/01_core.ipynb
class TextFont(Enum):
    "Combinations of TextT that are particularly useful"
    def __add__(self, other):   return stringify((self, other))
    def __radd__(self, other):  return stringify((other, self)) 
    def __str__(self): return self.value
    muted_sm = stringify((TextT.muted, TextT.small))
    muted_lg = stringify((TextT.muted, TextT.large))
    bold_sm = stringify((TextT.bold, TextT.small))
    

# %% ../lib_nbs/01_core.ipynb
class ButtonT(VEnum):
    "Options for styling Buttons"
    def _generate_next_value_(name, start, count, last_values): return str2ukcls('button', name)
    default = auto()
    primary = auto()
    secondary = auto()
    danger = auto()
    text = auto()
    link = auto()
    ghost = auto()

# %% ../lib_nbs/01_core.ipynb
def Button(*c: Union[str, FT],
           cls: Union[str, Enum]=ButtonT.default,
           submit=True,
           **kwargs
          ) -> FT:
    "A Button with Styling (defaults to `type=submit` for form submission)"
    return fh.Button(*c, cls=('uk-button', stringify(cls)), type='submit' if submit else 'button', **kwargs)

# %% ../lib_nbs/01_core.ipynb
def ButtonSubmit(*c: Union[str, FT],
           cls: Union[str, Enum]=ButtonT.default,
           **kwargs
          ) -> FT:
    "A Button with Styling to be used for submitting forms"
    return fh.Button(*c, cls=('uk-button', stringify(cls)), type='submit', **kwargs)

# %% ../lib_nbs/01_core.ipynb
def H1(*c:FT|str, cls:Enum|str|tuple=(), **kwargs)->FT: 
    "A H1 with Styling"
    return fh.H1(*c, cls=('uk-h1',stringify(cls)), **kwargs)

# %% ../lib_nbs/01_core.ipynb
def H2(*c:FT|str, cls:Enum|str|tuple=(), **kwargs)->FT: 
    "A H2 with Styling"
    return fh.H2(*c, cls=('uk-h2',stringify(cls)), **kwargs)

# %% ../lib_nbs/01_core.ipynb
def H3(*c:FT|str, cls:Enum|str|tuple=(), **kwargs)->FT: 
    "A H3 with Styling"
    return fh.H3(*c, cls=('uk-h3',stringify(cls)), **kwargs)

# %% ../lib_nbs/01_core.ipynb
def H4(*c:FT|str, cls:Enum|str|tuple=(), **kwargs)->FT:
    "A H4 with Styling"
    return fh.H4(*c, cls=('uk-h4',stringify(cls)), **kwargs)

# %% ../lib_nbs/01_core.ipynb
def Main(*args, **kwargs): return fh.Main(*args, **kwargs)

# %% ../lib_nbs/01_core.ipynb
def Titled(title:str="FastHTML app", *args, cls="container", **kwargs)->FT:
    "A H1 with styling, whose title is also used in the page's title tag"
    return fh.Title(title), fh.Main(H1(title), *args, cls=cls, **kwargs)

# %% ../lib_nbs/01_core.ipynb
class DividerT(VEnum):
    " Divider Styles from https://franken-ui.dev/docs/divider"
    def _generate_next_value_(name, start, count, last_values): return str2ukcls('divider', name)
    icon=auto()
    small=auto()
    vertical=auto()

# %% ../lib_nbs/01_core.ipynb
def Divider(*args, cls=('my-4', DividerT.icon), **kwargs):
    "Divider with default styling and margin"
    cls = stringify(cls)
    container = Div if 'uk-divider-vertical' in cls else Hr
    return container(*args, cls=cls, **kwargs)

# %% ../lib_nbs/01_core.ipynb
def DividerSplit(*c, cls=(), line_cls=(), text_cls=()):
    cls, line_cls, text_cls = map(stringify,(cls, line_cls, text_cls))
    return Div(cls='relative ' + cls)(
        Div(cls="absolute inset-0 flex items-center " + line_cls)(Span(cls="w-full border-t border-border")),
        Div(cls="relative flex justify-center " + text_cls)(Span(cls="bg-background px-2 ")(*c)))

# %% ../lib_nbs/01_core.ipynb
def DividerLine(lwidth=2, y_space=4): return Hr(cls=f"my-{y_space} h-[{lwidth}px] w-full bg-secondary")

# %% ../lib_nbs/01_core.ipynb
def Article(*c, cls=(), **kwargs):
    return fh.Article(*c, cls=('uk-article',stringify(cls)), **kwargs)

def ArticleTitle(*c, cls=(), **kwargs):
    return H1(*c, cls=('uk-article-title',stringify(cls)), **kwargs)

def ArticleMeta(*c, cls=(), **kwargs):
    return P(*c, cls=('uk-article-meta',stringify(cls)), **kwargs)

# %% ../lib_nbs/01_core.ipynb
class ContainerT(VEnum):
    'Max width container sizes from https://franken-ui.dev/docs/container'
    def _generate_next_value_(name, start, count, last_values): return str2ukcls('container', name)
    xsmall = auto()
    small = auto()
    large = auto()
    xlarge = auto()
    expand = auto()

# %% ../lib_nbs/01_core.ipynb
def Container(*c, cls=(), **kwargs): 
    "A Div to be used as a container that often wraps large sections or a page of content"
    return Div(*c, cls=('uk-container',stringify(cls)), **kwargs)


# %% ../lib_nbs/01_core.ipynb
class SectionT(VEnum):
    'Section styles from https://franken-ui.dev/docs/section'
    def _generate_next_value_(name, start, count, last_values): return str2ukcls('section', name)
    default = auto()
    muted = auto()
    primary = auto()
    secondary = auto()
    xsmall = auto()
    small = auto()
    large = auto()
    xlarge = auto()
    remove_vertical = auto()

# %% ../lib_nbs/01_core.ipynb
def Section(*c, cls=(), **kwargs):
    return fh.Div(*c, cls=('uk-section',stringify(cls)), **kwargs)

# %% ../lib_nbs/01_core.ipynb
def Fieldset(*c, cls=(), **kwargs): 
    return fh.Fieldset(*c, cls=('uk-fieldset',stringify(cls)), **kwargs)

def Legend(*c, cls=(), **kwargs): 
    return fh.Legend(*c, cls=('uk-legend',stringify(cls)), **kwargs)

# %% ../lib_nbs/01_core.ipynb
def Input(*c, cls=(), **kwargs):      
    return fh.Input(*c, cls=('uk-input',stringify(cls)), **kwargs)
def Select(*option, cls=(), **kwargs):
    return fh.Select(*option, cls=('uk-select',stringify(cls)), **kwargs)
def Radio(*c, cls=(), **kwargs):      
    return fh.Input(*c, cls=('uk-radio',stringify(cls)), type='radio', **kwargs)
def CheckboxX(*c, cls=(), **kwargs):  
    return fh.Input(*c, cls=('uk-checkbox',stringify(cls)), type='checkbox', **kwargs)
def Range(*c, cls=(), **kwargs):      
    return fh.Input(*c, cls=('uk-range',stringify(cls)), type='range', **kwargs)
def Toggle_switch(*c, cls=(), **kwargs):
    return fh.Input(*c, cls=('uk-toggle-switch uk-toggle-switch-primary',stringify(cls)), type='checkbox', **kwargs)
def TextArea(*c, cls=(), **kwargs):            
    return fh.Textarea(*c, cls=('uk-textarea',stringify(cls)), **kwargs)
def Switch(*c, cls='min-w-9', **kwargs):              
    return fh.Input(*c, cls=('uk-toggle-switch uk-toggle-switch-primary',stringify(cls)), type='checkbox', **kwargs)

# %% ../lib_nbs/01_core.ipynb
def FormLabel(*c, cls=(), **kwargs): return fh.Label(*c, cls=('uk-form-label',stringify(cls)), **kwargs)

# %% ../lib_nbs/01_core.ipynb
class LabelT(VEnum):
    def _generate_next_value_(name, start, count, last_values): return str2ukcls('label', name)
    primary = auto()
    secondary = auto()
    danger = auto()

# %% ../lib_nbs/01_core.ipynb
def Label(*c, cls=(), **kwargs):
    "FrankenUI labels, which look like pills"
    return fh.Label(*c, cls=('uk-label',stringify(cls)), **kwargs)

# %% ../lib_nbs/01_core.ipynb
def UkFormSection(title, description, *c, button_txt='Update', outer_margin=6, inner_margin=6):
    return Div(cls=f'space-y-{inner_margin} py-{outer_margin}')(
        Div(H3(title), P(description, cls=TextFont.muted_sm)),
        DividerSplit(), *c,
        Div(Button(button_txt, cls=ButtonT.primary)) if button_txt else None)

# %% ../lib_nbs/01_core.ipynb
def GenericLabelInput(
               label:str|FT,
               lbl_cls='',
               input_cls='',
               container=Div, 
               cls='',
               id='',
               input_fn=noop, 
                **kwargs
                ):
    "`Div(Label,Input)` component with Uk styling injected appropriately. Generally you should higher level API, such as `UkTextArea` which is created for you in this library"
    if isinstance(label, str) or label.tag != 'label': 
        label = FormLabel(cls=stringify(lbl_cls), fr=id)(label)
    inp = input_fn(id=id, cls=stringify(input_cls), **kwargs)        
    if container: return container(label, inp, cls=stringify(cls))
    return label, inp

# %% ../lib_nbs/01_core.ipynb
@delegates(GenericLabelInput, but=['input_fn','cls'])
def LabelInput(*args, cls='space-y-2', **kwargs): 
    "A Label and Input pair that provides default spacing and links/names them based on id"
    return GenericLabelInput(*args, cls=stringify(cls),input_fn=Input, **kwargs)

# %% ../lib_nbs/01_core.ipynb
def LabelRadio(label:str|FT,
               lbl_cls='',
               input_cls='',
               container=Div, 
               cls='flex items-center space-x-2',
               id='',
                **kwargs
                ):
    "A Label and Radio pair that provides default spacing and links/names them based on id"
    if isinstance(label, str) or label.tag != 'label': 
        label = FormLabel(cls=stringify(lbl_cls), fr=id)(label)
    inp = Radio(id=id, cls=stringify(input_cls), **kwargs)        
    if container: return container(inp, label, cls=stringify(cls))
    return inp, label

# %% ../lib_nbs/01_core.ipynb
def LabelCheckboxX(label:str|FT,
               lbl_cls='',
               input_cls='',
               container=Div, 
               cls='flex items-center space-x-2',
                **kwargs
                ):
    "`Div(Label,Input)` component with Uk styling injected appropriately. Generally you should higher level API, such as `UkTextArea` which is created for you in this library"
    
    id = kwargs.pop('id', fh.unqid())
    if isinstance(label, str) or label.tag != 'label': 
        label = FormLabel(cls=stringify(lbl_cls), fr=id)(label)
    inp = CheckboxX(id=id, cls=stringify(input_cls), **kwargs)        
    if container: return container(inp, label, cls=stringify(cls))
    return inp, label

# %% ../lib_nbs/01_core.ipynb
# @delegates(GenericLabelInput, but=['input_fn','cls'])
# def LabelCheckboxX(*args, cls='space-x-2', **kwargs): return GenericLabelInput(*args, cls=stringify(cls), input_fn=CheckboxX, **kwargs)

# %% ../lib_nbs/01_core.ipynb
@delegates(GenericLabelInput, but=['input_fn','cls'])
def LabelRange(*args, cls='space-y-2', **kwargs): return GenericLabelInput(*args, cls=stringify(cls), input_fn=Range, **kwargs)

# %% ../lib_nbs/01_core.ipynb
@delegates(GenericLabelInput, but=['input_fn','cls'])
def LabelTextArea(*args, cls='space-y-2', **kwargs): return GenericLabelInput(*args, cls=stringify(cls), input_fn=TextArea, **kwargs)

# %% ../lib_nbs/01_core.ipynb
@delegates(GenericLabelInput, but=['input_fn','cls'])
def LabelSwitch(*args, cls='space-x-2', **kwargs): return GenericLabelInput(*args, cls=stringify(cls), input_fn=Toggle_switch, **kwargs)

# %% ../lib_nbs/01_core.ipynb
def LabelSelect(*option,
               label:str|FT,
               lbl_cls='',
               input_cls='',
               container=Div, 
               cls='space-y-2',
               id='',
                **kwargs
                ):
    "`Div(Label,Input)` component with Uk styling injected appropriately. Generally you should higher level API, such as `UkTextArea` which is created for you in this library"
    if isinstance(label, str) or label.tag != 'label': 
        label = FormLabel(lbl_cls=stringify(lbl_cls), fr=id)(label)
    inp = Select(*option, id=id, cls=stringify(input_cls), **kwargs)        
    if container: return container(label, inp, cls=stringify(cls))
    return label, inp

# %% ../lib_nbs/01_core.ipynb
def Options(*c,                    # Content for an `Option`
            selected_idx:int=None, # Index location of selected `Option`
            disabled_idxs:set=None # Idex locations of disabled `Options`
           ):
    "Helper function to wrap things into `Option`s for use in `UkSelect`"
    return [fh.Option(o,selected=i==selected_idx, disabled=disabled_idxs and i in disabled_idxs) for i,o in enumerate(c)]

# %% ../lib_nbs/01_core.ipynb
def UkSelect(*option,            # Options for the select dropdown (can use `Options` helper function to create)
             inp_cls=(),         # Additional classes for the select input
             cls=('space-y-2',), # Classes for the outer div
             id="",              # ID for the select input
             name="",            # Name attribute for the select input
             placeholder="",     # Placeholder text for the select input
             searchable=False,   # Whether the select should be searchable
             **kwargs):          # Additional arguments passed to Uk_select
    "Creates a select dropdown with uk styling"
    inp_cls, cls = map(stringify, (inp_cls, cls))
    select = Uk_select(*option, cls=inp_cls, uk_cloak=True, id=id, 
                       name=name, placeholder=placeholder, searchable=searchable, **kwargs)
    return Div(cls=cls)(select)

# %% ../lib_nbs/01_core.ipynb
def LabelUkSelect(*option,            # Options for the select dropdown (can use `Options` helper function to create)
             label=(),           # String or FT component for the label
             lbl_cls=(),         # Additional classes for the label
             inp_cls=(),         # Additional classes for the select input
             cls=('space-y-2',), # Classes for the outer div
             id="",              # ID for the select input
             name="",            # Name attribute for the select input
             placeholder="",     # Placeholder text for the select input
             searchable=False,   # Whether the select should be searchable
             **kwargs):          # Additional arguments passed to Uk_select
    "Creates a select dropdown with uk styling"
    lbl_cls, inp_cls, cls = map(stringify, (lbl_cls, inp_cls, cls))
    if label: 
        lbl = FormLabel(cls=f'{lbl_cls}', fr=id)(label) 
    select = Uk_select(*option, cls=inp_cls, uk_cloak=True, id=id, 
                       name=name, placeholder=placeholder, searchable=searchable, **kwargs)
    return Div(cls=cls)(lbl, select) if label else Div(cls=cls)(select)

# %% ../lib_nbs/01_core.ipynb
class AT(VEnum):
    'Link styles from https://franken-ui.dev/docs/link'
    def _generate_next_value_(name, start, count, last_values): return str2ukcls('link', name)
    muted = auto()
    text = auto()
    reset = auto()

# %% ../lib_nbs/01_core.ipynb
# def Link(*c, cls=(), **kwargs):  
#     return fh.A(*c, cls=('uk-link',stringify(cls)), **kwargs)

# %% ../lib_nbs/01_core.ipynb
class ListT(VEnum):
    'List styles from https://franken-ui.dev/docs/list'
    def _generate_next_value_(name, start, count, last_values): return str2ukcls('list', name)
    disc = auto()
    circle = auto()
    square = auto()
    decimal = auto()
    hyphen = auto()
    muted = auto()
    primary = auto()
    secondary = auto()
    bullet = auto()
    divider = auto()
    striped = auto()

# %% ../lib_nbs/01_core.ipynb
def List(*c, cls=(), **kwargs): return fh.Ul(*c, cls=('uk-list',stringify(cls)), **kwargs)

# %% ../lib_nbs/01_core.ipynb
def ModalContainer(*c, cls=(), **kwargs):   return fh.Div(*c, cls=('uk-modal-container',stringify(cls)), uk_modal=True, **kwargs)
def ModalDialog(*c, cls=(), **kwargs):      return fh.Div(*c, cls=('uk-modal-dialog',   stringify(cls)),                **kwargs)
def ModalHeader(*c, cls=(), **kwargs):      return fh.Div(*c, cls=('uk-modal-header',   stringify(cls)),                **kwargs)
def ModalBody(*c, cls=(), **kwargs):        return fh.Div(*c, cls=('uk-modal-body',     stringify(cls)),                **kwargs)
def ModalFooter(*c, cls=(), **kwargs):      return fh.Div(*c, cls=('uk-modal-footer',   stringify(cls)),                **kwargs)
def ModalTitle(*c, cls=(), **kwargs):       return fh.H2(*c,  cls=('uk-modal-title',    stringify(cls)),                **kwargs)
def ModalCloseButton(*c, cls=(), **kwargs): return Button(*c, cls=('uk-modal-close',    stringify(cls)),                **kwargs)

# %% ../lib_nbs/01_core.ipynb
def Modal(*c,
        header=None,          # Components that go in the header
        footer=None,          # Components that go in the footer
        cls=(),               # class for outermost container
        dialog_cls=(),        # classes for the dialog
        header_cls='p-6',     # classes for the header
        body_cls='space-y-6', # classes for the body
        footer_cls=(),        # classes for the footer
        id='',                # id for the outermost container
        **kwargs              # classes for the outermost container
        ): # Modal
    "Create a Modal using the appropriate Modal* classes to put the boilerplate in the appropriate places for you"
    cls, dialog_cls, header_cls, body_cls, footer_cls = map(stringify, (cls, dialog_cls, header_cls, body_cls, footer_cls))
    res = []
    if header: res.append(ModalHeader(cls=header_cls)(header))
    res.append(ModalBody(cls=body_cls)(*c))
    if footer: res.append(ModalFooter(cls=footer_cls)(footer))
    return ModalContainer(ModalDialog(*res, cls=dialog_cls), cls=cls, id=id, **kwargs)

# %% ../lib_nbs/01_core.ipynb
class PaddingT(VEnum):
    'Padding Modifiers from https://franken-ui.dev/docs/padding'
    def _generate_next_value_(name, start, count, last_values): return str2ukcls('padding', name)
    xsmall = auto()
    small = auto()
    default = ''
    medium = auto()
    large = auto()
    xlarge = auto()
    remove = auto()
    remove_top = auto()
    remove_bottom = auto()
    remove_left = auto()
    remove_right = auto()
    remove_vertical = auto()
    remove_horizontal = auto()

# %% ../lib_nbs/01_core.ipynb
class PositionT(VEnum):
    'Position modifiers from https://franken-ui.dev/docs/position'
    def _generate_next_value_(name, start, count, last_values): return str2ukcls('position', name)
    top = auto()
    bottom = auto()
    left = auto()
    right = auto()
    top_left = auto()
    top_center = auto()
    top_right = auto()
    center = auto()
    center_left = auto()
    center_right = auto()
    bottom_left = auto()
    bottom_center = auto()
    bottom_right = auto()
    center_horizontal = auto()
    center_vertical = auto()

# %% ../lib_nbs/01_core.ipynb
def Placeholder(*c, cls=(), **kwargs):
    return fh.Div(*c, cls=('uk-placeholder',stringify(cls)), **kwargs)

# %% ../lib_nbs/01_core.ipynb
def Progress(*c, cls=(), value="", max="", **kwargs):
    return fh.Progress(*c, value=value, max=max, cls=('uk-progress',stringify(cls)), **kwargs)

# %% ../lib_nbs/01_core.ipynb
def UkIcon(icon,height=None,width=None,stroke_width=None,cls=(), **kwargs):
    return Uk_icon(icon=icon, height=height, width=width, stroke_width=stroke_width, cls=cls, **kwargs)

# %% ../lib_nbs/01_core.ipynb
def UkIconLink(icon, 
           height=None,
           width=None,
           stroke_width=None,
           cls=(), 
           button=False, 
           **kwargs):
    
    fn = fh.Button if button else fh.A
    return fh.A(cls=(f"uk-icon-{'button' if button else 'link'}", stringify(cls)), **kwargs)(
        UkIcon(icon=icon, height=height, width=width, stroke_width=stroke_width))

# %% ../lib_nbs/01_core.ipynb
def DiceBearAvatar(seed_name, # Seed name (ie 'Isaac Flath')
                   h=20,         # Height 
                   w=20,          # Width
                  ):          # Span with Avatar
    url = 'https://api.dicebear.com/8.x/lorelei/svg?seed='
    return Span(cls=f"relative flex h-{h} w-{w} shrink-0 overflow-hidden rounded-full bg-accent")(
            fh.Img(cls=f"aspect-square h-{h} w-{w}", alt="Avatar", loading="lazy", src=f"{url}{seed_name}"))

# %% ../lib_nbs/01_core.ipynb
class FlexT(VEnum):
    'Flexbox modifiers from UIkit'
    def _generate_next_value_(name, start, count, last_values): return str2ukcls('flex', name)
    
    # Display
    block, inline = 'uk-flex', auto()
    # Horizontal Alignment
    left, center, right, between, around = auto(), auto(), auto(), auto(), auto()
    # Vertical Alignment
    stretch, top, middle, bottom = auto(), auto(), auto(), auto()
    # Direction
    row, row_reverse, column, column_reverse = auto(), auto(), auto(), auto()
    # Wrap
    nowrap, wrap, wrap_reverse = auto(), auto(), auto()

# %% ../lib_nbs/01_core.ipynb
def Grid(*div,         # Divs/Containers that should be divided into a grid
         cols_min=None, # defaults to min(len(div),1)
         cols_sm=None, # defaults to min(len(div),2)
         cols_md=None, # defaults to min(len(div),3)
         cols_lg=None, # defaults to min(len(div),4)
         cols=None,    # Size at every breakpoint
         cls='gap-4',  # Additional classes for Grid Div
         **kwargs      # Additional args for Grid Div
        ):
    """Creates a grid with the given number of columns, often used for a grid of cards"""
    cols_min = cols_min if cols_min else cols if cols else 1
    cols_sm = cols_sm if cols_sm else cols if cols else max(min(len(div), 2), cols_min+1)
    cols_md = cols_md if cols_md else cols if cols else max(min(len(div), 3), cols_min+2)
    cols_lg = cols_lg if cols_lg else cols if cols else max(min(len(div), 3), cols_min+2)
    cls = stringify(cls)
    return Div(cls=(f'grid grid-cols-{cols_min} sm:grid-cols-{cols_sm} md:grid-cols-{cols_md} lg:grid-cols-{cols_lg}',cls), **kwargs)(*div)

# %% ../lib_nbs/01_core.ipynb
def DivFullySpaced(*c,                # Components
                   cls='uk-width-1-1',# Classes for outer div
                   **kwargs           # Additional args for outer div
                  ):                  # Div with spaced components via flex classes
    "Creates a flex div with it's components having as much space between them as possible"
    cls = stringify(cls)
    return Div(cls=(FlexT.block,FlexT.between,FlexT.middle,cls), **kwargs)(*c)

# %% ../lib_nbs/01_core.ipynb
def DivCentered(*c,      # Components
                cls='space-y-4',  # Classes for outer div
                **kwargs # Additional args for outer div
               ): # Div with components centered in it
    "Creates a flex div with it's components centered in it"
    cls=stringify(cls)
    return Div(cls=(FlexT.block,FlexT.column,FlexT.middle,FlexT.center,cls),**kwargs)(*c)

# %% ../lib_nbs/01_core.ipynb
def DivLAligned(*c,      # Components
                cls='space-x-4',  # Classes for outer div
                **kwargs # Additional args for outer div
               ): # Div with components aligned to the left
    "Creates a flex div with it's components aligned to the left"
    cls=stringify(cls)
    return Div(cls=(FlexT.block,FlexT.left,FlexT.middle,cls), **kwargs)(*c)

# %% ../lib_nbs/01_core.ipynb
def DivRAligned(*c,      # Components
                cls='space-x-4',  # Classes for outer div
                **kwargs # Additional args for outer div
               ): # Div with components aligned to the right
    "Creates a flex div with it's components aligned to the right"
    cls=stringify(cls)
    return Div(cls=(FlexT.block,FlexT.right,FlexT.middle,cls), **kwargs)(*c)

# %% ../lib_nbs/01_core.ipynb
def DivVStacked(*c, cls='space-y-4', **kwargs):
    cls=stringify(cls)
    return Div(cls=(FlexT.block,FlexT.column,FlexT.middle,cls), **kwargs)(*c)

# %% ../lib_nbs/01_core.ipynb
def DivHStacked(*c, cls='space-x-4', **kwargs):
    cls=stringify(cls)
    return Div(cls=(FlexT.block,FlexT.row,FlexT.middle,cls), **kwargs)(*c)

# %% ../lib_nbs/01_core.ipynb
class NavT(VEnum):
    def _generate_next_value_(name, start, count, last_values): return str2ukcls('nav', name)
    default = auto()
    primary = auto()
    secondary = auto()

# %% ../lib_nbs/01_core.ipynb
def NavContainer(*li, 
                 cls=NavT.primary,
                 parent=True, 
                 uk_nav=False, #True for default collapsible behavior, see https://franken-ui.dev/docs/nav#component-options for more advanced options
                 **kwargs):
    return fh.Ul(*li, uk_nav=uk_nav, cls=(f"uk-nav{'' if parent else '-sub'}", stringify(cls)),**kwargs)

# %% ../lib_nbs/01_core.ipynb
def NavParentLi(*nav_container, cls=(), **kwargs): return fh.Li(*nav_container,  cls=('uk-parent',  stringify(cls)),**kwargs)
def NavDividerLi(*c,cls=(), **kwargs): return fh.Li(*c, cls=('uk-nav-divider', stringify(cls)),**kwargs)
def NavHeaderLi(*c,cls=(), **kwargs): return fh.Li(*c, cls=('uk-nav-header', stringify(cls)),**kwargs)
def NavSubtitle(*c,cls=TextFont.muted_sm, **kwargs): return fh.Div(*c, cls=('uk-nav-subtitle', stringify(cls)),**kwargs)
def NavCloseLi(*c,cls=(), **kwargs): return fh.Li(*c, cls=('uk-drop-close', stringify(cls)),**kwargs)

# %% ../lib_nbs/01_core.ipynb
def NavBarContainer(*c, 
                    cls=(),
                    container_cls=ContainerT.expand,
                    uk_navbar=True,
                    **kwargs): 
    return fh.Div(Container(Div(*c, uk_navbar=uk_navbar),cls=stringify(container_cls)), cls=('',stringify(cls)), **kwargs) #uk-navbar-container
def NavBarLSide(*c,  cls=(), **kwargs): return fh.Div(*c, cls=('uk-navbar-left',  stringify(cls)), **kwargs)
def NavBarRSide(*c,  cls=(), **kwargs): return fh.Div(*c, cls=('uk-navbar-right', stringify(cls)), **kwargs)
def NavBarCenter(*c, cls=(), **kwargs): return fh.Div(*c, cls=('uk-navbar-center',stringify(cls)), **kwargs)

# %% ../lib_nbs/01_core.ipynb
def NavBarNav(*li, cls=(), **kwargs): return fh.Nav(*li, cls=('uk-navbar-nav',      stringify(cls)),                 **kwargs)

# %% ../lib_nbs/01_core.ipynb
def NavBarSubtitle(title, subtitle, cls=(), subtitle_cls=TextFont.muted_sm, **kwargs): 
    return fh.Div(title,fh.Div(subtitle, cls=('uk-navbar-subtitle', stringify(subtitle_cls))), cls=stringify(cls), **kwargs)

# %% ../lib_nbs/01_core.ipynb
def NavBarNavContainer(*li, 
                       cls=NavT.primary,
                         parent=True, 
                         uk_nav=False, #True for default collapsible behavior, see https://franken-ui.dev/docs/nav#component-options for more advanced options
                         **kwargs):
    return Div(cls="uk-navbar-dropdown")(NavContainer(*li, cls=('uk-navbar-dropdown-nav',stringify(cls)), uk_nav=uk_nav, parent=parent, **kwargs))

# %% ../lib_nbs/01_core.ipynb
def NavBarParentIcon(): return Span(uk_navbar_parent_icon=True)

# %% ../lib_nbs/01_core.ipynb
def DropDownNavContainer(*li, 
                         cls=NavT.primary,
                         parent=True, 
                         uk_nav=False, #True for default collapsible behavior, see https://franken-ui.dev/docs/nav#component-options for more advanced options
                         uk_dropdown=True,
                         **kwargs):
    return Div(cls = 'uk-drop uk-dropdown',uk_dropdown=uk_dropdown)(NavContainer(*li, cls=('uk-dropdown-nav',stringify(cls)), uk_nav=uk_nav, parent=parent, **kwargs))

# %% ../lib_nbs/01_core.ipynb
def TabContainer(*li,cls='', alt=False, **kwargs):
    cls = stringify(cls)
    return Ul(cls=(f"uk-tab{'-alt' if alt else ''}",stringify(cls)),**kwargs)(*li)

# %% ../lib_nbs/01_core.ipynb
class CardT(VEnum):
    'Card styles from UIkit'
    def _generate_next_value_(name, start, count, last_values): return str2ukcls('card', name)
    default = auto()
    primary = auto()
    secondary = auto()
    danger = auto()

# %% ../lib_nbs/01_core.ipynb
def CardTitle(*c, cls=(), **kwargs):
    return fh.Div(*c, cls=('uk-card-title',stringify(cls)), **kwargs)

def CardHeader(*c, cls=(), **kwargs):
    return fh.Div(*c, cls=('uk-card-header',stringify(cls)), **kwargs)

def CardBody(*c, cls=(), **kwargs):
    return fh.Div(*c, cls=('uk-card-body',stringify(cls)), **kwargs)

def CardFooter(*c, cls=(), **kwargs):
    return fh.Div(*c, cls=('uk-card-footer',stringify(cls)), **kwargs)

def CardContainer(*c, cls=CardT.default, **kwargs):
    return fh.Div(*c, cls=('uk-card',stringify(cls)), **kwargs)

# %% ../lib_nbs/01_core.ipynb
def Card(*c, # Components that go in the body
        header=None, # Components that go in the header
        footer=None,  # Components that go in the footer
        body_cls='space-y-6', # classes for the body
        header_cls=(), # classes for the header
        footer_cls=(), # classes for the footer
        cls=(), #class for outermost component
        **kwargs # classes that for the card itself
        ):
    header_cls, footer_cls, body_cls, cls = map(stringify, (header_cls, footer_cls, body_cls, cls))
    res = []
    if header: res.append(CardHeader(cls=header_cls)(header))
    res.append(CardBody(cls=body_cls)(*c))
    if footer: res.append(CardFooter(cls=footer_cls)(footer))
    return CardContainer(cls=cls, **kwargs)(*res)

# %% ../lib_nbs/01_core.ipynb
class TableT(VEnum):
    def _generate_next_value_(name, start, count, last_values): return str2ukcls('table', name)
    divider = auto()
    striped = auto()
    hover = auto()
    small = auto()
    large = auto()
    justify = auto()
    middle = auto()
    responsive = auto()

# %% ../lib_nbs/01_core.ipynb
def Table(*args, cls=(TableT.middle, TableT.divider, TableT.hover, TableT.small), **kwargs): 
    return fh.Table(cls=('uk-table', stringify(cls)), *args, **kwargs)

# %% ../lib_nbs/01_core.ipynb
def _TableCell(Component, *args, cls=(), shrink=False, expand=False, small=False, **kwargs):
    cls = stringify(cls)
    if shrink: cls += ' uk-table-shrink'
    if expand: cls += ' uk-table-expand'
    if small: cls += ' uk-table-small'
    return Component(*args,cls=cls, **kwargs)

@delegates(_TableCell, but=['Component'])
def Td(*args,**kwargs):  return _TableCell(fh.Td, *args, **kwargs)
@delegates(_TableCell, but=['Component'])
def Th(*args,**kwargs): return _TableCell(fh.Th, *args, **kwargs)

def Tr(*cells, cls=(), **kwargs):  return fh.Tr(*cells, cls=stringify(cls), **kwargs)
def Thead(*rows, cls=(), **kwargs): return fh.Thead(*rows, cls=stringify(cls), **kwargs)
def Tbody(*rows, cls=(), sortable=False, **kwargs): return fh.Tbody(*rows, cls=stringify(cls), uk_sortable=sortable, **kwargs)

# %% ../lib_nbs/01_core.ipynb
def TableFromLists(header_data, body_data, footer_data=None, 
                   header_cell_render=Th,body_cell_render=Td, footer_cell_render=Td,
                   cls=(TableT.middle, TableT.divider, TableT.hover, TableT.small), 
                   sortable=False, **kwargs):
    
    return Table(
                Thead(Tr(*map(header_cell_render, header_data))),
                Tbody(*[Tr(*map(body_cell_render, r)) for r in body_data], sortable=sortable),
                Tfoot(Tr(*map(footer_cell_render, footer_data))) if footer_data else '',
                cls=stringify(cls),    
                **kwargs)

# %% ../lib_nbs/01_core.ipynb
def TableFromDicts(header_data:Sequence, body_data:Sequence[dict], footer_data=None, 
                   header_cell_render=Th, body_cell_render=lambda k,v : Td(v), footer_cell_render=lambda k,v : Td(v),
                   cls=(TableT.middle, TableT.divider, TableT.hover, TableT.small),
                   sortable=False,
                   **kwargs):
    
    return Table(
        Thead(Tr(*[header_cell_render(h) for h in header_data])),
        Tbody(*[Tr(*[body_cell_render(k, r.get(k, '')) for k in header_data]) for r in body_data], sortable=sortable),
        Tfoot(Tr(*[footer_cell_render(k, footer_data.get(k.lower(), '')) for k in header_data])) if footer_data else '',
        cls=stringify(cls),    
        **kwargs
    )

# %% ../lib_nbs/01_core.ipynb
def apply_classes(html_str:str, 
                  class_map=None, 
                  class_map_mods=None):
    from lxml import html, etree
    if not class_map:
        class_map = {
            'h1': 'uk-h1 my-4 mb-4',
            'h2': 'uk-h2 my-8',
            'h3': 'uk-h3 my-8',
            'h4': 'uk-h4 my-8',
            'ul': "uk-list uk-list-disc mb-4",
            'a': "uk-link",
            'p': 'my-1',
            'blockquote': "uk-blockquote mb-8",
            'hr':'uk-divider-icon my-4',
            'table':'uk-table-middle uk-table-divider uk-table-hover uk-table-small'
        }

    if class_map_mods: class_map = {**class_map, **class_map_mods}
    html_str = html.fromstring(html_str)
    for tag, classes in class_map.items():
        for element in html_str.xpath(f'//{tag}'):
            existing_class = element.get('class', '')
            new_class = f"{existing_class} {classes}".strip()
            element.set('class', new_class)
    return etree.tostring(html_str, encoding='unicode', method='html')

# %% ../lib_nbs/01_core.ipynb
def render_md(md_content):
    try: import markdown2
    except ImportError: raise ImportError("Install 'markdown2' to use the 'render_md' function")
    html_content = markdown2.markdown(md_content)
    styled_html = apply_classes(html_content)
    return NotStr(styled_html)
