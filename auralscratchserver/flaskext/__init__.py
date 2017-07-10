from .dated_url_for import DatedUrlForExtension
from .static_file_mixins import StaticFileMixinsExtension
from .context_constants import ContextConstantsExtension

extensions = [DatedUrlForExtension(), StaticFileMixinsExtension(), ContextConstantsExtension()]
