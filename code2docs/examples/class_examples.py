"""Class usage examples for code2docs."""

from generators.module_docs_gen import ModuleDocsGenerator
from generators.readme_gen import ReadmeGenerator
from generators.examples_gen import ExamplesGenerator
from generators.api_reference_gen import ApiReferenceGenerator
from analyzers.docstring_extractor import DocstringExtractor


# --- ModuleDocsGenerator ---
# Generate docs/modules/ — detailed per-module documentation.
instance = ModuleDocsGenerator(config=..., result=...)
instance.generate_all()
instance.write_all(output_dir=..., files=...)

# --- ReadmeGenerator ---
# Generate README.md from AnalysisResult.
instance = ReadmeGenerator(config=..., result=...)
instance.generate()
instance.write(path=..., content=...)

# --- ExamplesGenerator ---
# Generate examples/ — usage examples from public API signatures.
instance = ExamplesGenerator(config=..., result=...)
instance.generate_all()
instance.write_all(output_dir=..., files=...)

# --- ApiReferenceGenerator ---
# Generate docs/api/ — per-module API reference from signatures.
instance = ApiReferenceGenerator(config=..., result=...)
instance.generate_all()
instance.write_all(output_dir=..., files=...)

# --- DocstringExtractor ---
# Extract and parse docstrings from AnalysisResult.
instance = DocstringExtractor()
instance.extract_all(result=...)
instance.parse(docstring=...)
instance.coverage_report(result=...)
