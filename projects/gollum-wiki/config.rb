require "rubygems"

Gollum::Page::FORMAT_NAMES = { :markdown  => 'Markdown' }
=begin
Valid formats are:
{ :markdown  => 'Markdown',
  :textile   => 'Textile',
  :rdoc      => 'RDoc',
  :org       => 'Org-mode',
  :creole    => 'Creole',
  :rest      => 'reStructuredText',
  :asciidoc  => 'AsciiDoc',
  :mediawiki => 'MediaWiki',
  :pod       => 'Pod' }
=end

require 'omnigollum'
require 'omniauth'
require 'omniauth-github'

options = {
    :providers => Proc.new do
        provider :github, ENV['GITHUB_ID'], ENV['GITHUB_SECRET']
    end,
    :dummy_auth => false,
    :author_format => Proc.new { |user| user.name },
    :auther_email => Proc.new { |user| user.email},
    :authorized_users => ENV['AUTHORIZED_EMAIL'],
#    :authorized_users => ENV['GOLLUM_AUTHORIZED_USERS'].split(','),
    :protected_routes => [
        '/revert/*',
        '/revert',
        '/create/*',
        '/create',
        '/edit/*',
        '/edit',
        '/rename/*',
        '/rename'
    ]
}

Precious::App.set(:omnigollum, options)

Precious::App.register Omnigollum::Sinatra

Precious::App.set(:wiki_options, {
    :live_preview => false,
    :css => true,
    :allow_editing => true,
    :h1_title => false,
})
