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
        # Only trigger within JavaScript
        if not view.match_selector(locations[0],
                "source.js"):
            return []

        pt = locations[0] - len(prefix) - 1
        ch = view.substr(sublime.Region(pt, pt + 1))
        if ch != '.':
            return []
        # We try to escape the cases when we have g_form. and don't mix the functions of g_form with the Glide
        ptGformEscape = locations[0] - len(prefix) - 7
        chGformEscape = view.substr(sublime.Region(ptGformEscape, ptGformEscape + 7))
        if chGformEscape == 'g_form.':
            return []
        if chGformEscape == 'g_user.':
            return []

        return ([
                # GlideRecord Query
                ("addActiveQuery()", "addActiveQuery()"),
                ("addDomainQuery(Object o)", "addDomainQuery($1)"),
                ("addEncodedQuery(String query)", "addEncodedQuery($1)"),
                ("addInactiveQuery()", "addInactiveQuery()"),
                ("addJoinQuery(joinTable, [primaryField], [joinTableField])", "addJoinQuery($1)"),
                ("addNotNullQuery(String fieldName)", "addNotNullQuery($1)"),
                ("addNullQuery(String fieldName)", "addNullQuery($1)"),
                ("addOrCondition(String fieldName, [Object operator], Object value)", "addOrCondition($1,$2)"),
                ("addQuery(String fieldName, [Object operator], Object value)", "addQuery($1,$2)"),
                ("canCreate()", "canCreate()"),
                ("canDelete()", "canDelete()"),
                ("canRead()", "canRead()"),
                ("canWrite()", "canWrite()"),
                ("changes()", "changes()"),
                ("find(columnName, value)", "find($1, $2)"),
                ("hasAttachments()", "hasAttachments()"),
                ("hasNext()", "hasNext()"),
                ("instanceOf(String className)", "instanceOf($1)"),
                ("isNewRecord()", "isNewRecord()"),
                ("isValid()", "isValid()"),
                ("isValidField(String columnName)", "isValidField($1)"),
                ("isValidRecord()", "isValidRecord()"),
                ("next()", "next()"),
                ("_next()", "_next()"),
                ("operation()", "operation()"),
                ("orderBy(String name)", "orderBy($1)"),
                ("orderByDesc(String name)", "orderByDesc($1)"),
                ("query([Object field, Object value])", "query()"),
                ("queryNoDomain([Object field, Object value])", "queryNoDomain()"),
                ("_query([Object field, Object value])", "_query()"),
                ("restoreLocation()", "restoreLocation()"),
                ("saveLocation()", "saveLocation()"),

                # GlideRecord Get
                ("get(Object name, Object value)", "get($1, $2)"),
                ("getAttribute(String attribute)", "getAttribute($1)"),
                ("getClassDisplayValue()", "getClassDisplayValue()"),
                ("getDisplayValue()", "getDisplayValue()"),
                ("getED()", "getED()"),
                ("getElement(String columnName)", "getElement($1)"),
                ("getEncodedQuery()", "getEncodedQuery()"),
                ("getEscapedDisplayValue()", "getEscapedDisplayValue()"),
                ("getFields()", "getFields()"),
                ("getLabel()", "getLabel()"),
                ("getLink(boolean noStack)", "getLink($1)"),
                ("getLocation()", "getLocation()"),
                ("getPlural()", "getPlural()"),
                ("getRecordClassName()", "getRecordClassName()"),
                ("getRelatedLists()", "getRelatedLists()"),
                ("getRelatedTables()", "getRelatedTables()"),
                ("getRowCount()", "getRowCount()"),
                ("getRowNumber()", "getRowNumber()"),
                ("getTableName()", "getTableName()"),
                ("getValue(String name)", "getValue($1)"),

                # GlideRecord Set
                ("autoSysFields(boolean e)", "autoSysFields($1)"),
                ("setAbortAction(boolean b)", "setAbortAction($1)"),
                ("setDisplayValue(String name, Object value)", "setDisplayValue($1)"),
                ("setForceUpdate(boolean force)", "setForceUpdate($1)"),
                ("setLimit(int)", "setLimit($1)"),
                ("setLocation(int rowNumber)", "setLocation($1)"),
                ("setNewGuid()", "setNewGuid()"),
                ("setNewGuidValue(String guid)", "setNewGuidValue($1)"),
                ("setQueryReferences(boolean queryReferences)", "setQueryReferences($1)"),
                ("setUseEngines(boolean e)", "setUseEngines($1)"),
                ("setValue(String name, Object value)", "setValue($1,$2)"),
                ("setWorkflow(boolean e)", "setWorkflow($1)"),
                

                # GlideRecord Update
                ("applyTemplate(String template)", "applyTemplate($1)"),
                ("update(Object reason)", "update($1)"),
                ("updateWithReferences(Object reason)", "updateWithReferences($1)"),

                # GlideRecord Insert
                ("initialize()", "initialize()"),
                ("insert()", "insert()"),
                ("insertWithReferences()", "insertWithReferences()"),
                ("newRecord()", "newRecord()"),
                ("deleteMultiple()", "deleteMultiple()"),

                #GlideRecord Delete
                ("deleteMultiple()", "deleteMultiple()"),
                ("deleteRecord()", "deleteRecord()")

        ], sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)
