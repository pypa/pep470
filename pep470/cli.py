# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os.path

try:
    from urllib import parse as urllib_parse
except ImportError:
    import urlparse as urllib_parse

import click
import pip.index
import pip.download
import progress.bar


@click.command()
@click.argument("projects", nargs=-1, required=True)
def pep470(projects):
    session = pip.download.PipSession()
    session.timeout = 5
    session.auth.prompting = False

    finder = pip.index.PackageFinder(
        [],
        ["https://pypi.python.org/simple/"],
        allow_all_external=True,
        allow_unverified=projects,
        allow_all_prereleases=True,
        session=session,
    )

    for project in progress.bar.Bar("Downloading").iter(projects):
        try:
            all_versions = finder._find_all_versions(project)
        except Exception:
            click.echo("Skipping {}, an error occured.".format(project))
            continue

        seen = set()
        urls = set()
        for version in all_versions:
            if version.version not in seen:
                seen.add(version.version)
                if not version.location.internal:
                    urls.add(version.location.url)

        for url in urls:
            try:
                resp = session.get(url)
                resp.raise_for_status()

                o = urllib_parse.urlparse(url)

                try:
                    os.makedirs("dist")
                except Exception:
                    pass

                path = os.path.join("dist", os.path.basename(o.path))
                with open(path, "wb") as fp:
                    fp.write(resp.content)

            except Exception:
                click.echo("Skipping {}, an error occured.".format(url))
                continue

    click.echo(
        "Downloaded all externally hosted files, upload to PyPI using `twine "
        "upload --skip-existing dist/*`"
    )
