import sublime, sublime_plugin
import re

def match(rex, str):
    m = rex.match(str)
    if m:
        return m.group(0)
    else:
        return None


# Provide completions that match just after typing an opening angle bracket
class TagCompletions(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        # Only trigger within HTML
        if not view.match_selector(locations[0],
                "source.js"):
            return []

        pt = locations[0] - len(prefix) - 1
        ch = view.substr(sublime.Region(pt, pt + 1))
        if ch != '.':
            return []

        return ([
                # GlideRecord Query
                ("addActiveQuery()", "addActiveQuery()"),
                ("addDomainQuery(Object o)", "addDomainQuery($0)"),
                ("addEncodedQuery(String query)", "addEncodedQuery($0)"),
                ("addInactiveQuery()", "addInactiveQuery()"),
                ("addJoinQuery(joinTable, [primaryField], [joinTableField])", "addJoinQuery($0)"),
                ("addNotNullQuery(String fieldName)", "addNotNullQuery($0)"),
                ("addNullQuery(String fieldName)", "addNullQuery($0)"),
                ("addOrCondition(String fieldName, [Object operator], Object value)", "addOrCondition($0,$1)"),
                ("addQuery(String fieldName, [Object operator], Object value)", "addQuery($0,$1)"),
                ("canCreate()", "canCreate()"),
                ("canDelete()", "canDelete()"),
                ("canRead()", "canRead()"),
                ("canWrite()", "canWrite()"),
                ("changes()", "changes()"),
                ("find(columnName, value)", "find($0, $1)"),
                ("hasAttachments()", "hasAttachments()"),
                ("hasNext()", "hasNext()"),
                ("instanceOf(String className)", "instanceOf($0)"),
                ("isNewRecord()", "isNewRecord()"),
                ("isValid()", "isValid()"),
                ("isValidField(String columnName)", "isValidField($0)"),
                ("isValidRecord()", "isValidRecord()"),
                ("next()", "next()"),
                ("_next()", "_next()"),
                ("operation()", "operation()"),
                ("orderBy(String name)", "orderBy($0)"),
                ("orderByDesc(String name)", "orderByDesc($0)"),
                ("query([Object field, Object value])", "query()"),
                ("queryNoDomain([Object field, Object value])", "queryNoDomain()"),
                ("_query([Object field, Object value])", "_query()"),
                ("restoreLocation()", "restoreLocation()"),
                ("saveLocation()", "saveLocation()"),

                # GlideRecord Get
                ("get(Object name, Object value)", "get($0, $1)"),
                ("getAttribute(String attribute)", "getAttribute($0)"),
                ("getClassDisplayValue()", "getClassDisplayValue()"),
                ("getDisplayValue()", "getDisplayValue()"),
                ("getED()", "getED()"),
                ("getElement(String columnName)", "getElement($0)"),
                ("getEncodedQuery()", "getEncodedQuery()"),
                ("getEscapedDisplayValue()", "getEscapedDisplayValue()"),
                ("getFields()", "getFields()"),
                ("getLabel()", "getLabel()"),
                ("getLink(boolean noStack)", "getLink($0)"),
                ("getLocation()", "getLocation()"),
                ("getPlural()", "getPlural()"),
                ("getRecordClassName()", "getRecordClassName()"),
                ("getRelatedLists()", "getRelatedLists()"),
                ("getRelatedTables()", "getRelatedTables()"),
                ("getRowCount()", "getRowCount()"),
                ("getRowNumber()", "getRowNumber()"),
                ("getTableName()", "getTableName()"),
                ("getValue(String name)", "getValue($0)")
        ], sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)
